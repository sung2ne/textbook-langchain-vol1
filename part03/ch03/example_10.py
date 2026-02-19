summary_template = ChatPromptTemplate.from_messages([
    ("system", "당신은 문서 요약 전문가입니다."),
    ("human", """다음 텍스트를 {max_sentences}문장으로 요약해주세요.

텍스트:
{text}

요약:""")
])
