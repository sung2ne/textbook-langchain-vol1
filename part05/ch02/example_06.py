from langchain_community.chat_message_histories import SQLChatMessageHistory

# SQLite 데이터베이스에 저장
history = SQLChatMessageHistory(
    session_id="user123",
    connection_string="sqlite:///chat_history.db"
)

history.add_user_message("안녕하세요")
history.add_ai_message("안녕하세요! 도와드릴까요?")

# 프로그램을 재시작해도 대화가 유지됩니다
