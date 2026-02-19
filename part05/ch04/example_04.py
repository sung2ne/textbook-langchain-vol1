from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.output_parsers import StrOutputParser
from langchain_core.chat_history import InMemoryChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory
import uuid

class MultiSessionChatbot:
    def __init__(self):
        self.llm = ChatOllama(model="llama4")
        self.sessions = {}

        self.prompt = ChatPromptTemplate.from_messages([
            ("system", "당신은 친절한 AI 어시스턴트입니다."),
            MessagesPlaceholder(variable_name="history"),
            ("human", "{input}")
        ])

        self.chain = self.prompt | self.llm | StrOutputParser()

        self.chatbot = RunnableWithMessageHistory(
            self.chain,
            self._get_session_history,
            input_messages_key="input",
            history_messages_key="history"
        )

    def _get_session_history(self, session_id: str):
        if session_id not in self.sessions:
            self.sessions[session_id] = InMemoryChatMessageHistory()
        return self.sessions[session_id]

    def create_session(self) -> str:
        """새 세션 생성"""
        session_id = str(uuid.uuid4())[:8]
        self.sessions[session_id] = InMemoryChatMessageHistory()
        return session_id

    def chat(self, session_id: str, message: str) -> str:
        """메시지 전송"""
        config = {"configurable": {"session_id": session_id}}
        return self.chatbot.invoke({"input": message}, config=config)

    def get_history(self, session_id: str):
        """세션 히스토리 조회"""
        if session_id in self.sessions:
            return self.sessions[session_id].messages
        return []

    def clear_session(self, session_id: str):
        """세션 초기화"""
        if session_id in self.sessions:
            self.sessions[session_id].clear()

    def delete_session(self, session_id: str):
        """세션 삭제"""
        if session_id in self.sessions:
            del self.sessions[session_id]

    def list_sessions(self):
        """모든 세션 목록"""
        return list(self.sessions.keys())


# 사용
bot = MultiSessionChatbot()

# 사용자 A
session_a = bot.create_session()
print(f"Session A: {session_a}")
print(bot.chat(session_a, "내 이름은 철수야"))

# 사용자 B (별도 세션)
session_b = bot.create_session()
print(f"\nSession B: {session_b}")
print(bot.chat(session_b, "내 이름은 영희야"))

# 각자 자신의 이름만 기억
print(f"\nSession A: {bot.chat(session_a, '내 이름이 뭐야?')}")
print(f"Session B: {bot.chat(session_b, '내 이름이 뭐야?')}")
