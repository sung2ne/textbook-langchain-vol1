from langchain_ollama import ChatOllama
from langchain_core.messages import SystemMessage, HumanMessage

llm = ChatOllama(model="llama4")

messages = [
    SystemMessage(content="당신은 친절한 Python 튜터입니다. 초보자도 이해할 수 있게 쉽게 설명해주세요."),
    HumanMessage(content="for 루프가 뭐야?")
]

response = llm.invoke(messages)
print(response.content)
