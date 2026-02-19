from langchain_ollama import ChatOllama
from langchain_core.messages import SystemMessage, HumanMessage

class ConversationMemory:
    def __init__(self, system_prompt, max_messages=10):
        self.system_message = SystemMessage(content=system_prompt)
        self.messages = []
        self.max_messages = max_messages

    def add_user_message(self, content):
        self.messages.append(HumanMessage(content=content))
        self._trim()

    def add_ai_message(self, message):
        self.messages.append(message)
        self._trim()

    def _trim(self):
        # 최대 개수 초과 시 오래된 메시지 삭제
        if len(self.messages) > self.max_messages:
            self.messages = self.messages[-self.max_messages:]

    def get_messages(self):
        return [self.system_message] + self.messages

    def clear(self):
        self.messages = []


# 사용
llm = ChatOllama(model="llama4")
memory = ConversationMemory(
    system_prompt="당신은 친절한 어시스턴트입니다.",
    max_messages=6
)

def chat(user_input):
    memory.add_user_message(user_input)
    response = llm.invoke(memory.get_messages())
    memory.add_ai_message(response)
    return response.content

# 테스트
print(chat("안녕! 내 이름은 철수야."))
print(chat("내 취미는 프로그래밍이야."))
print(chat("내 이름이 뭐야?"))
print(chat("내 취미가 뭐야?"))
