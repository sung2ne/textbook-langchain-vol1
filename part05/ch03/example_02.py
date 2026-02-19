import tiktoken

class TokenBasedMemory:
    def __init__(self, max_tokens: int = 2000, model: str = "gpt-4o"):
        self.messages = []
        self.max_tokens = max_tokens
        self.encoder = tiktoken.encoding_for_model(model)

    def add_message(self, message):
        self.messages.append(message)
        self._trim()

    def _count_tokens(self, messages):
        total = 0
        for msg in messages:
            total += len(self.encoder.encode(msg.content))
        return total

    def _trim(self):
        while self._count_tokens(self.messages) > self.max_tokens and len(self.messages) > 1:
            self.messages.pop(0)  # 가장 오래된 메시지 삭제

    def get_messages(self):
        return self.messages
