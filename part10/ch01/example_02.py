from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

messages = [
    SystemMessage(content="당신은 도움이 되는 AI입니다."),
    HumanMessage(content="안녕하세요"),
    AIMessage(content="안녕하세요! 무엇을 도와드릴까요?")
]
