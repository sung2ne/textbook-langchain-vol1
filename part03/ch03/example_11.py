review_template = ChatPromptTemplate.from_messages([
    ("system", """당신은 코드 리뷰 전문가입니다.

다음 관점에서 리뷰해주세요:
- 가독성
- 성능
- 보안
- 모범 사례 준수"""),
    ("human", """언어: {language}

{code}

리뷰해주세요.""")
])
