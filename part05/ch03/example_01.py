from langchain_core.chat_history import InMemoryChatMessageHistory
from langchain_core.messages import HumanMessage, AIMessage

class WindowMemory:
    def __init__(self, max_messages: int = 10):
        self.history = InMemoryChatMessageHistory()
        self.max_messages = max_messages

    def add_user_message(self, content: str):
        self.history.add_user_message(content)
        self._trim()

    def add_ai_message(self, content: str):
        self.history.add_ai_message(content)
        self._trim()

    def _trim(self):
        messages = self.history.messages
        if len(messages) > self.max_messages:
            # 오래된 메시지 삭제
            self.history.messages = messages[-self.max_messages:]

    def get_messages(self):
        return self.history.messages

    def clear(self):
        self.history.clear()


# 사용
memory = WindowMemory(max_messages=6)  # 최근 6개만 유지

memory.add_user_message("1번 메시지")
memory.add_ai_message("1번 응답")
memory.add_user_message("2번 메시지")
memory.add_ai_message("2번 응답")
memory.add_user_message("3번 메시지")
memory.add_ai_message("3번 응답")
memory.add_user_message("4번 메시지")  # 이 시점에서 1번 메시지 삭제

print(f"저장된 메시지 수: {len(memory.get_messages())}")  # 6
