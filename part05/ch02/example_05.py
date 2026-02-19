from langchain_core.chat_history import InMemoryChatMessageHistory

class SessionManager:
    def __init__(self):
        self.sessions = {}

    def get_history(self, session_id: str) -> InMemoryChatMessageHistory:
        if session_id not in self.sessions:
            self.sessions[session_id] = InMemoryChatMessageHistory()
        return self.sessions[session_id]

    def clear_session(self, session_id: str):
        if session_id in self.sessions:
            self.sessions[session_id].clear()

    def delete_session(self, session_id: str):
        if session_id in self.sessions:
            del self.sessions[session_id]

    def list_sessions(self):
        return list(self.sessions.keys())


# 사용
manager = SessionManager()

# 사용자 A의 대화
history_a = manager.get_history("user_a")
history_a.add_user_message("안녕")

# 사용자 B의 대화 (별도 히스토리)
history_b = manager.get_history("user_b")
history_b.add_user_message("Hello")

print(f"활성 세션: {manager.list_sessions()}")  # ['user_a', 'user_b']
