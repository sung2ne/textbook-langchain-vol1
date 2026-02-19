from langchain_ollama import ChatOllama
from langchain_core.messages import SystemMessage, HumanMessage

llm = ChatOllama(model="llama4")

# 대화 기록 저장
conversation = [
    SystemMessage(content="당신은 친절한 AI 어시스턴트입니다.")
]

def chat(user_input):
    # 사용자 메시지 추가
    conversation.append(HumanMessage(content=user_input))

    # LLM 호출
    response = llm.invoke(conversation)

    # AI 응답 저장
    conversation.append(response)

    return response.content

# 대화 테스트
print(chat("안녕! 나는 철수야."))
print(chat("내 이름이 뭐라고 했지?"))
