from langchain_ollama import ChatOllama
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.prompts import ChatPromptTemplate

llm = ChatOllama(model="llama4")
parser = JsonOutputParser()

template = ChatPromptTemplate.from_messages([
    ("system", "JSON 형식으로 응답하세요."),
    ("human", """{topic}에 대해 다음 형식으로 알려주세요:
{{"name": "이름", "description": "설명", "examples": ["예시1", "예시2"]}}""")
])

chain = template | llm | parser

result = chain.invoke({"topic": "Python 리스트"})
print(type(result))  # <class 'dict'>
print(result)
