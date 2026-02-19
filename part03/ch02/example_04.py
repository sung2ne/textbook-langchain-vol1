from langchain_ollama import ChatOllama
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

llm = ChatOllama(model="llama4")

messages = [
    SystemMessage(content="당신은 Python 튜터입니다."),
    HumanMessage(content="변수가 뭐야?"),
    AIMessage(content="변수는 값을 저장하는 공간입니다. x = 10처럼 사용합니다."),
    HumanMessage(content="예시 더 보여줘")  # 현재 질문
]

response = llm.invoke(messages)
print(response.content)
