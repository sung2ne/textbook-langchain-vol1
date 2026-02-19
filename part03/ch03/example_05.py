from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate

llm = ChatOllama(model="llama4")

template = ChatPromptTemplate.from_messages([
    ("system", "당신은 {language} 전문가입니다."),
    ("human", "{concept}에 대해 설명해주세요.")
])

# 방법 1: format_messages + invoke
messages = template.format_messages(language="Python", concept="데코레이터")
response = llm.invoke(messages)
print(response.content)
