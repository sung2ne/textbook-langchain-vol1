from langchain_ollama import ChatOllama
from langchain_core.messages import SystemMessage, HumanMessage

llm = ChatOllama(model="llama4")

# 시스템 프롬프트를 바꿔보세요
system_prompts = [
    "당신은 해적입니다. 해적처럼 말하세요.",
    "당신은 셰익스피어입니다. 고풍스럽게 말하세요.",
    "당신은 5살 아이입니다. 천진난만하게 말하세요.",
]

question = "날씨가 좋은데 뭐하면 좋을까?"

for prompt in system_prompts:
    print(f"[{prompt[:20]}...]")
    messages = [
        SystemMessage(content=prompt),
        HumanMessage(content=question)
    ]
    response = llm.invoke(messages)
    print(f"{response.content}\n")
