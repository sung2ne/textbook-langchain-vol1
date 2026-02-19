# 단순 템플릿
prompt = ChatPromptTemplate.from_template("질문: {question}")

# 채팅 템플릿
prompt = ChatPromptTemplate.from_messages([
    ("system", "당신은 {role}입니다."),
    ("human", "{question}")
])
