from langchain_ollama import ChatOllama
from langchain_core.output_parsers import CommaSeparatedListOutputParser
from langchain_core.prompts import ChatPromptTemplate

llm = ChatOllama(model="llama4")
parser = CommaSeparatedListOutputParser()

template = ChatPromptTemplate.from_messages([
    ("human", """{topic}의 예시 5개를 쉼표로 구분해서 나열해주세요.
{format_instructions}""")
])

chain = template | llm | parser

result = chain.invoke({
    "topic": "프로그래밍 언어",
    "format_instructions": parser.get_format_instructions()
})

print(type(result))  # <class 'list'>
print(result)        # ['Python', 'JavaScript', 'Java', 'C++', 'Go']
