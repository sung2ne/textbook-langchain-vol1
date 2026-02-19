from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.output_parsers import StrOutputParser
from langchain_core.chat_history import InMemoryChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory

# LLM 설정
llm = ChatOllama(model="llama4")

# 프롬프트 설정
prompt = ChatPromptTemplate.from_messages([
    ("system", """당신은 친절하고 도움이 되는 AI 어시스턴트입니다.

사용자의 질문에 정확하고 유용한 답변을 제공하세요.
이전 대화 내용을 기억하고 자연스럽게 대화를 이어가세요.
"""),
    MessagesPlaceholder(variable_name="history"),
    ("human", "{input}")
])

# 체인 구성
chain = prompt | llm | StrOutputParser()

# 세션 저장소
store = {}

def get_session_history(session_id: str):
    if session_id not in store:
        store[session_id] = InMemoryChatMessageHistory()
    return store[session_id]

# 히스토리 연결
chatbot = RunnableWithMessageHistory(
    chain,
    get_session_history,
    input_messages_key="input",
    history_messages_key="history"
)

def main():
    session_id = "default"
    config = {"configurable": {"session_id": session_id}}

    print("=" * 50)
    print("AI 챗봇에 오신 것을 환영합니다!")
    print("종료하려면 'quit' 또는 'exit'를 입력하세요.")
    print("대화 기록을 지우려면 'clear'를 입력하세요.")
    print("=" * 50)

    while True:
        try:
            user_input = input("\n👤 You: ").strip()

            if not user_input:
                continue

            if user_input.lower() in ["quit", "exit", "q"]:
                print("안녕히 가세요!")
                break

            if user_input.lower() == "clear":
                store[session_id] = InMemoryChatMessageHistory()
                print("대화 기록이 초기화되었습니다.")
                continue

            # 스트리밍 응답
            print("\n🤖 AI: ", end="", flush=True)
            for chunk in chatbot.stream({"input": user_input}, config=config):
                print(chunk, end="", flush=True)
            print()

        except KeyboardInterrupt:
            print("\n\n안녕히 가세요!")
            break

if __name__ == "__main__":
    main()
