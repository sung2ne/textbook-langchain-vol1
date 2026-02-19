import streamlit as st
from chatbot import ProductChatbot

st.set_page_config(page_title="상품 비교 챗봇", page_icon="🛒", layout="wide")

if "chatbot" not in st.session_state:
    st.session_state.chatbot = ProductChatbot()

st.title("🛒 상품 비교 챗봇")

# 탭 생성
tab_chat, tab_products, tab_compare, tab_analyze = st.tabs([
    "💬 채팅", "📦 상품 목록", "⚖️ 비교", "📊 분석"
])

# 채팅 탭
with tab_chat:
    if "messages" not in st.session_state:
        st.session_state.messages = []

    for msg in st.session_state.messages:
        st.chat_message(msg["role"]).write(msg["content"])

    if prompt := st.chat_input("질문하세요..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        st.chat_message("user").write(prompt)

        with st.spinner("생각 중..."):
            response = st.session_state.chatbot.chat(prompt)

        st.session_state.messages.append({"role": "assistant", "content": response})
        st.chat_message("assistant").write(response)

# 상품 목록 탭
with tab_products:
    st.subheader("등록된 상품")

    col1, col2 = st.columns([3, 1])
    with col2:
        if st.button("테스트 상품 추가"):
            st.session_state.chatbot.add_test_products()
            st.rerun()

    products = st.session_state.chatbot.store.get_all()

    if not products:
        st.info("등록된 상품이 없습니다. 테스트 상품을 추가해보세요.")
    else:
        for p in products:
            with st.container():
                col1, col2, col3 = st.columns([3, 1, 1])
                with col1:
                    st.write(f"**{p.name}**")
                with col2:
                    st.write(f"{p.price:,}원")
                with col3:
                    if st.button("삭제", key=f"del_{p.url}"):
                        st.session_state.chatbot.store.remove(p.url)
                        st.rerun()

# 비교 탭
with tab_compare:
    st.subheader("상품 비교")

    products = st.session_state.chatbot.store.get_all()

    if len(products) < 2:
        st.warning("비교하려면 2개 이상의 상품이 필요합니다.")
    else:
        if st.button("비교 분석 실행"):
            with st.spinner("분석 중..."):
                result = st.session_state.chatbot.analyzer.compare_text(products)
            st.markdown(result)

# 분석 탭
with tab_analyze:
    st.subheader("개별 상품 분석")

    products = st.session_state.chatbot.store.get_all()

    if not products:
        st.info("분석할 상품이 없습니다.")
    else:
        selected = st.selectbox(
            "상품 선택",
            options=range(len(products)),
            format_func=lambda i: products[i].name
        )

        if st.button("분석 실행"):
            with st.spinner("분석 중..."):
                result = st.session_state.chatbot.analyzer.analyze(products[selected])

            col1, col2 = st.columns(2)
            with col1:
                st.write("**👍 장점**")
                for pro in result.get("pros", []):
                    st.write(f"- {pro}")
            with col2:
                st.write("**👎 단점**")
                for con in result.get("cons", []):
                    st.write(f"- {con}")

            st.write(f"**🎯 추천 대상**: {result.get('target_user', 'N/A')}")
            st.write(f"**💰 가성비**: {result.get('value_rating', 'N/A')}")
