from langchain_ollama import ChatOllama
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

llm = ChatOllama(model="llama4")

# 대화 기록 저장
conversation = [
    SystemMessage(content="당신은 친절한 어시스턴트입니다.")
]

def chat(user_input):
    # 사용자 메시지 추가
    conversation.append(HumanMessage(content=user_input))

    # 전체 대화 기록과 함께 호출
    response = llm.invoke(conversation)

    # AI 응답 저장
    conversation.append(response)

    return response.content

# 테스트
print(chat("내 이름은 철수야"))
# → 안녕하세요, 철수님! 만나서 반갑습니다.

print(chat("내 이름이 뭐라고 했지?"))
# → 철수님이라고 하셨어요!
