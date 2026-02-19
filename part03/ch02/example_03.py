messages = [
    SystemMessage(content="당신은 친절한 멘토입니다. 칭찬과 함께 개선점을 부드럽게 제안하세요."),
    HumanMessage(content="""다음 코드를 리뷰해줘.

def add(a, b):
    return a + b
""")
]

response = llm.invoke(messages)
print(response.content)
