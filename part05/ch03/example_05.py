from langchain_ollama import ChatOllama
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

class PracticalMemory:
    def __init__(self, llm, buffer_size: int = 6, summary_threshold: int = 10):
        self.llm = llm
        self.buffer = []  # 최근 메시지
        self.summary = ""  # 오래된 대화 요약
        self.buffer_size = buffer_size
        self.summary_threshold = summary_threshold
        self.message_count = 0

    def add_exchange(self, user_msg: str, ai_msg: str):
        self.buffer.append(HumanMessage(content=user_msg))
        self.buffer.append(AIMessage(content=ai_msg))
        self.message_count += 2

        # 버퍼가 넘치면 요약
        if len(self.buffer) > self.buffer_size:
            self._summarize_old_messages()

    def _summarize_old_messages(self):
        # 오래된 메시지 추출
        old = self.buffer[:-self.buffer_size]
        self.buffer = self.buffer[-self.buffer_size:]

        # 요약 업데이트
        conv_text = "\n".join([
            f"{'User' if isinstance(m, HumanMessage) else 'AI'}: {m.content}"
            for m in old
        ])

        prompt = f"""
현재 요약: {self.summary if self.summary else '없음'}

추가된 대화:
{conv_text}

위 내용을 통합하여 핵심 정보만 1-2문장으로 요약해주세요.
사용자의 이름, 관심사, 요청사항 등 중요한 정보를 포함하세요.
"""
        response = self.llm.invoke(prompt)
        self.summary = response.content

    def get_context_messages(self):
        messages = []
        if self.summary:
            messages.append(SystemMessage(
                content=f"[이전 대화 요약]\n{self.summary}"
            ))
        messages.extend(self.buffer)
        return messages


# 사용 예시
llm = ChatOllama(model="llama4")
memory = PracticalMemory(llm, buffer_size=4)

def chat(user_input):
    # 컨텍스트와 함께 LLM 호출
    messages = [
        SystemMessage(content="당신은 친절한 어시스턴트입니다.")
    ] + memory.get_context_messages() + [
        HumanMessage(content=user_input)
    ]

    response = llm.invoke(messages)

    # 메모리 업데이트
    memory.add_exchange(user_input, response.content)

    return response.content
