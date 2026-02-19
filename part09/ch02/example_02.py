import streamlit as st
from chatbot import ProductChatbot
from models import Product

# 페이지 설정
st.set_page_config(
    page_title="상품 비교 챗봇",
    page_icon="🛒",
    layout="wide"
)

# 세션 상태 초기화
if "chatbot" not in st.session_state:
    st.session_state.chatbot = ProductChatbot()

if "messages" not in st.session_state:
    st.session_state.messages = []


def main():
    st.title("🛒 상품 비교 챗봇")

    # 사이드바 - 상품 관리
    with st.sidebar:
        st.header("📦 상품 관리")

        # 테스트 데이터 추가
        if st.button("테스트 상품 추가"):
            result = st.session_state.chatbot.add_test_products()
            st.success(result)

        # 상품 목록
        products = st.session_state.chatbot.store.get_all()
        st.subheader(f"등록된 상품 ({len(products)}개)")

        for i, p in enumerate(products, 1):
            with st.expander(f"{i}. {p.name}"):
                st.write(f"💰 {p.price:,}원")
                if p.specs:
                    for k, v in p.specs.items():
                        st.write(f"- {k}: {v}")

        # 전체 삭제
        if products and st.button("전체 삭제", type="secondary"):
            st.session_state.chatbot.store.clear()
            st.rerun()

    # 메인 영역 - 채팅
    st.header("💬 대화")

    # 이전 메시지 표시
    for msg in st.session_state.messages:
        role = msg["role"]
        content = msg["content"]

        if role == "user":
            st.chat_message("user").write(content)
        else:
            st.chat_message("assistant").write(content)

    # 입력
    if prompt := st.chat_input("질문을 입력하세요..."):
        # 사용자 메시지 추가
        st.session_state.messages.append({"role": "user", "content": prompt})
        st.chat_message("user").write(prompt)

        # AI 응답
        with st.spinner("생각 중..."):
            response = st.session_state.chatbot.process(prompt)

        st.session_state.messages.append({"role": "assistant", "content": response})
        st.chat_message("assistant").write(response)


if __name__ == "__main__":
    main()
