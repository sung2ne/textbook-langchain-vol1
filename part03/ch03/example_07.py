from langchain_core.prompts import ChatPromptTemplate

template = ChatPromptTemplate.from_messages([
    ("system", "당신은 {language} 전문가입니다."),
    ("human", "{question}")
])

# language만 미리 설정
python_template = template.partial(language="Python")

# question만 나중에 제공
messages = python_template.format_messages(question="클래스가 뭐야?")
