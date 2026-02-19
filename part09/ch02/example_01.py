import streamlit as st

st.title("Hello, Streamlit!")
st.write("첫 번째 Streamlit 앱입니다.")

# 입력
name = st.text_input("이름을 입력하세요")
if name:
    st.write(f"안녕하세요, {name}님!")

# 버튼
if st.button("클릭!"):
    st.balloons()
