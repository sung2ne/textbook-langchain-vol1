from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.chat_history import InMemoryChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory

llm = ChatOllama(model="llama4")

# 프롬프트에 대화 기록 자리 마련
prompt = ChatPromptTemplate.from_messages([
    ("system", "당신은 친절한 어시스턴트입니다."),
    MessagesPlaceholder(variable_name="history"),  # 대화 기록이 들어갈 자리
    ("human", "{input}")
])

chain = prompt | llm

# 세션별 히스토리 저장소
store = {}

def get_session_history(session_id: str):
    if session_id not in store:
        store[session_id] = InMemoryChatMessageHistory()
    return store[session_id]

# 히스토리 연결
chain_with_history = RunnableWithMessageHistory(
    chain,
    get_session_history,
    input_messages_key="input",
    history_messages_key="history"
)

# 사용 (세션 ID 지정)
config = {"configurable": {"session_id": "user123"}}

response1 = chain_with_history.invoke(
    {"input": "내 이름은 철수야"},
    config=config
)
print(response1.content)

response2 = chain_with_history.invoke(
    {"input": "내 이름이 뭐야?"},
    config=config
)
print(response2.content)
