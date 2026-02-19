from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate

llm = ChatOllama(model="llama4")

template = ChatPromptTemplate.from_messages([
    ("system", "당신은 {language} 전문가입니다."),
    ("human", "{concept}에 대해 설명해주세요.")
])

# 체인 연결 (다음 장에서 자세히 배웁니다)
chain = template | llm

response = chain.invoke({
    "language": "Python",
    "concept": "제너레이터"
})
print(response.content)
