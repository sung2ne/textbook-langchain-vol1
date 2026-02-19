from langchain_ollama import ChatOllama
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

class StreamingChatbot:
    def __init__(self, model: str = "llama4", system_prompt: str = None):
        self.llm = ChatOllama(model=model)
        self.system_prompt = system_prompt or "당신은 친절한 AI 어시스턴트입니다."
        self.history = []

    def chat(self, user_input: str) -> str:
        # 메시지 구성
        messages = [SystemMessage(content=self.system_prompt)]
        messages.extend(self.history)
        messages.append(HumanMessage(content=user_input))

        # 스트리밍 응답
        full_response = ""
        print("🤖 AI: ", end="", flush=True)

        for chunk in self.llm.stream(messages):
            content = chunk.content
            print(content, end="", flush=True)
            full_response += content

        print()

        # 히스토리 업데이트
        self.history.append(HumanMessage(content=user_input))
        self.history.append(AIMessage(content=full_response))

        # 히스토리 제한 (최근 10개)
        if len(self.history) > 10:
            self.history = self.history[-10:]

        return full_response

    def clear_history(self):
        self.history = []


# 사용
bot = StreamingChatbot(system_prompt="당신은 Python 튜터입니다.")

while True:
    user_input = input("\n👤 You: ").strip()
    if user_input.lower() in ["quit", "exit"]:
        break
    bot.chat(user_input)
