from langchain_core.chat_history import InMemoryChatMessageHistory


class OptimizedChatHistory(InMemoryChatMessageHistory):
    def __init__(self, max_messages: int = 20):
        super().__init__()
        self.max_messages = max_messages

    def add_message(self, message):
        super().add_message(message)

        # 최대 개수 초과 시 오래된 메시지 삭제
        if len(self.messages) > self.max_messages:
            # 시스템 메시지는 유지
            system_msgs = [m for m in self.messages if m.type == "system"]
            other_msgs = [m for m in self.messages if m.type != "system"]

            # 최근 메시지만 유지
            keep = self.max_messages - len(system_msgs)
            self.messages = system_msgs + other_msgs[-keep:]
