from langchain_ollama import ChatOllama
from langchain_core.chat_history import InMemoryChatMessageHistory
from langchain_core.messages import SystemMessage

llm = ChatOllama(model="llama4")
history = InMemoryChatMessageHistory()

SYSTEM_PROMPT = "당신은 친절한 AI 어시스턴트입니다."

def chat(user_input):
    # 사용자 메시지 저장
    history.add_user_message(user_input)

    # 시스템 메시지 + 히스토리
    messages = [SystemMessage(content=SYSTEM_PROMPT)] + history.messages

    # LLM 호출
    response = llm.invoke(messages)

    # AI 응답 저장
    history.add_ai_message(response.content)

    return response.content

# 테스트
print(chat("내 이름은 영희야"))
print(chat("내 이름이 뭐야?"))
