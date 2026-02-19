from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.output_parsers import StrOutputParser
from langchain_core.chat_history import InMemoryChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory

def create_expert_chatbot(expert_type: str):
    """전문가 유형에 따른 챗봇 생성"""

    expert_prompts = {
        "python": """당신은 10년 경력의 Python 개발자입니다.

역할:
- 코드 예시와 함께 설명합니다
- 모범 사례를 안내합니다
- 초보자도 이해할 수 있게 설명합니다

응답 형식:
- 먼저 개념을 설명합니다
- 코드 예시를 제공합니다
- 주의사항이나 팁을 추가합니다""",

        "english": """당신은 영어 선생님입니다.

역할:
- 영어 문법과 표현을 가르칩니다
- 틀린 문장을 교정해줍니다
- 자연스러운 표현을 알려줍니다

응답 형식:
- 올바른 표현을 제시합니다
- 왜 그런지 설명합니다
- 예문을 제공합니다""",

        "fitness": """당신은 전문 피트니스 트레이너입니다.

역할:
- 운동 방법을 안내합니다
- 식단 조언을 제공합니다
- 안전한 운동을 강조합니다

주의:
- 의학적 조언은 제공하지 않습니다
- 전문의 상담을 권장합니다"""
    }

    system_prompt = expert_prompts.get(expert_type, "당신은 친절한 어시스턴트입니다.")

    llm = ChatOllama(model="llama4")
    prompt = ChatPromptTemplate.from_messages([
        ("system", system_prompt),
        MessagesPlaceholder(variable_name="history"),
        ("human", "{input}")
    ])

    chain = prompt | llm | StrOutputParser()

    store = {}

    def get_history(session_id):
        if session_id not in store:
            store[session_id] = InMemoryChatMessageHistory()
        return store[session_id]

    return RunnableWithMessageHistory(
        chain,
        get_history,
        input_messages_key="input",
        history_messages_key="history"
    )


# 사용
print("전문가를 선택하세요: python, english, fitness")
expert = input("선택: ").strip().lower()

chatbot = create_expert_chatbot(expert)
config = {"configurable": {"session_id": "user1"}}

while True:
    user_input = input("\n👤 You: ").strip()
    if user_input.lower() in ["quit", "exit"]:
        break

    response = chatbot.invoke({"input": user_input}, config=config)
    print(f"\n🤖 Expert: {response}")
