messages = [
    SystemMessage(content="당신은 엄격한 시니어 개발자입니다. 코드의 문제점을 날카롭게 지적하세요."),
    HumanMessage(content="""다음 코드를 리뷰해줘.

def add(a, b):
    return a + b
""")
]

response = llm.invoke(messages)
print(response.content)
