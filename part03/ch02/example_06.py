from langchain_core.messages import SystemMessage, HumanMessage

messages = [
    SystemMessage(content="당신은 Python 튜터입니다."),
    HumanMessage(content="변수가 뭐야?")
]
