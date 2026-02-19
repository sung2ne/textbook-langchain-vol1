from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# 컴포넌트 생성
prompt = ChatPromptTemplate.from_messages([
    ("system", "당신은 친절한 어시스턴트입니다."),
    ("human", "{question}")
])
llm = ChatOllama(model="llama4")
parser = StrOutputParser()

# 체인 생성
chain = prompt | llm | parser

# 실행
result = chain.invoke({"question": "Python이 뭐야?"})
print(result)
