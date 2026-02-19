from langchain_core.chat_history import InMemoryChatMessageHistory
from langchain_core.messages import HumanMessage, AIMessage

# 히스토리 생성
history = InMemoryChatMessageHistory()

# 메시지 추가
history.add_user_message("안녕하세요")
history.add_ai_message("안녕하세요! 무엇을 도와드릴까요?")
history.add_user_message("Python이 뭐야?")

# 메시지 확인
for msg in history.messages:
    print(f"[{msg.type}] {msg.content}")
