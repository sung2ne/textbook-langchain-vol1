from langchain_ollama import ChatOllama
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

class SummaryMemory:
    def __init__(self, llm, max_messages: int = 6):
        self.llm = llm
        self.summary = ""
        self.recent_messages = []
        self.max_messages = max_messages

    def add_user_message(self, content: str):
        self.recent_messages.append(HumanMessage(content=content))
        self._check_and_summarize()

    def add_ai_message(self, content: str):
        self.recent_messages.append(AIMessage(content=content))
        self._check_and_summarize()

    def _check_and_summarize(self):
        if len(self.recent_messages) > self.max_messages:
            # 오래된 메시지들 요약
            old_messages = self.recent_messages[:-self.max_messages]
            self._update_summary(old_messages)
            # 최근 메시지만 유지
            self.recent_messages = self.recent_messages[-self.max_messages:]

    def _update_summary(self, messages):
        # 기존 요약 + 새 메시지 → 새 요약
        conversation_text = "\n".join([
            f"{'사용자' if isinstance(m, HumanMessage) else 'AI'}: {m.content}"
            for m in messages
        ])

        prompt = f"""
기존 요약: {self.summary if self.summary else '없음'}

새로운 대화:
{conversation_text}

위 내용을 통합하여 중요한 정보만 간결하게 요약해주세요.
"""

        response = self.llm.invoke(prompt)
        self.summary = response.content

    def get_messages(self):
        messages = []
        if self.summary:
            messages.append(SystemMessage(
                content=f"이전 대화 요약: {self.summary}"
            ))
        messages.extend(self.recent_messages)
        return messages

    def clear(self):
        self.summary = ""
        self.recent_messages = []


# 사용
llm = ChatOllama(model="llama4")
memory = SummaryMemory(llm, max_messages=4)

# 긴 대화 시뮬레이션
conversations = [
    ("내 이름은 철수야", "안녕하세요, 철수님!"),
    ("내 취미는 프로그래밍이야", "프로그래밍 좋아하시는군요!"),
    ("Python을 주로 사용해", "Python은 좋은 선택입니다."),
    ("최근에 LangChain을 배우고 있어", "LangChain 재밌죠!"),
    ("오늘 날씨가 좋아", "산책하기 좋겠네요!"),
]

for user_msg, ai_msg in conversations:
    memory.add_user_message(user_msg)
    memory.add_ai_message(ai_msg)

# 요약 확인
print(f"요약: {memory.summary}")
print(f"최근 메시지 수: {len(memory.recent_messages)}")
