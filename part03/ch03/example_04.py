from langchain_core.prompts import ChatPromptTemplate

# 대화형 템플릿 생성
template = ChatPromptTemplate.from_messages([
    ("system", "당신은 {role}입니다. {style}로 답변해주세요."),
    ("human", "{question}")
])

# 템플릿 적용
messages = template.format_messages(
    role="Python 전문가",
    style="간결하게",
    question="리스트와 튜플의 차이점은?"
)

print(messages)
