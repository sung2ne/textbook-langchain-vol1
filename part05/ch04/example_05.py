# chatbot.py

from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.output_parsers import StrOutputParser
from langchain_core.chat_history import InMemoryChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory

class Chatbot:
    def __init__(
        self,
        model: str = "llama4",
        system_prompt: str = None,
        max_history: int = 10
    ):
        self.llm = ChatOllama(model=model)
        self.system_prompt = system_prompt or "당신은 친절한 AI 어시스턴트입니다."
        self.max_history = max_history
        self.store = {}

        self.prompt = ChatPromptTemplate.from_messages([
            ("system", self.system_prompt),
            MessagesPlaceholder(variable_name="history"),
            ("human", "{input}")
        ])

        self.chain = self.prompt | self.llm | StrOutputParser()

        self.chatbot = RunnableWithMessageHistory(
            self.chain,
            self._get_history,
            input_messages_key="input",
            history_messages_key="history"
        )

    def _get_history(self, session_id: str):
        if session_id not in self.store:
            self.store[session_id] = InMemoryChatMessageHistory()
        return self.store[session_id]

    def _trim_history(self, session_id: str):
        if session_id in self.store:
            messages = self.store[session_id].messages
            if len(messages) > self.max_history:
                self.store[session_id].messages = messages[-self.max_history:]

    def chat(self, message: str, session_id: str = "default") -> str:
        config = {"configurable": {"session_id": session_id}}
        response = self.chatbot.invoke({"input": message}, config=config)
        self._trim_history(session_id)
        return response

    def stream(self, message: str, session_id: str = "default"):
        config = {"configurable": {"session_id": session_id}}
        for chunk in self.chatbot.stream({"input": message}, config=config):
            yield chunk
        self._trim_history(session_id)

    def clear(self, session_id: str = "default"):
        if session_id in self.store:
            self.store[session_id].clear()


# 사용 예시
if __name__ == "__main__":
    bot = Chatbot(
        system_prompt="당신은 Python 전문가입니다.",
        max_history=6
    )

    print("챗봇을 시작합니다. 종료: quit")

    while True:
        user_input = input("\nYou: ").strip()
        if user_input.lower() in ["quit", "exit"]:
            break

        print("AI: ", end="", flush=True)
        for chunk in bot.stream(user_input):
            print(chunk, end="", flush=True)
        print()
