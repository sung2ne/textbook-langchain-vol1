from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.output_parsers import StrOutputParser
from langchain_core.chat_history import InMemoryChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory

# 컴포넌트 설정
llm = ChatOllama(model="llama4")
parser = StrOutputParser()

prompt = ChatPromptTemplate.from_messages([
    ("system", "당신은 친절한 AI 어시스턴트입니다. 사용자의 이름을 기억하고 자연스럽게 대화해주세요."),
    MessagesPlaceholder(variable_name="history"),
    ("human", "{input}")
])

chain = prompt | llm | parser

# 세션 저장소
store = {}

def get_session_history(session_id: str):
    if session_id not in store:
        store[session_id] = InMemoryChatMessageHistory()
    return store[session_id]

# 메모리 연결
chat_chain = RunnableWithMessageHistory(
    chain,
    get_session_history,
    input_messages_key="input",
    history_messages_key="history"
)

# 대화 함수
def chat(session_id: str, message: str) -> str:
    config = {"configurable": {"session_id": session_id}}
    return chat_chain.invoke({"input": message}, config=config)

# 테스트
print(chat("user1", "안녕! 나는 철수야."))
print(chat("user1", "내 이름이 뭐야?"))
print(chat("user1", "오늘 Python 공부하려고 해."))
print(chat("user1", "내가 뭘 공부한다고 했지?"))
