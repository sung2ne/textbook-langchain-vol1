from langchain_ollama import ChatOllama
from langchain_core.output_parsers import PydanticOutputParser
from langchain_core.prompts import ChatPromptTemplate
from pydantic import BaseModel, Field
from typing import List

# 출력 형식 정의
class BookInfo(BaseModel):
    title: str = Field(description="책 제목")
    author: str = Field(description="저자")
    year: int = Field(description="출판 연도")
    genres: List[str] = Field(description="장르 목록")

llm = ChatOllama(model="llama4")
parser = PydanticOutputParser(pydantic_object=BookInfo)

template = ChatPromptTemplate.from_messages([
    ("system", "도서 정보를 JSON 형식으로 제공하세요."),
    ("human", """{book_name}에 대한 정보를 알려주세요.

{format_instructions}""")
])

chain = template | llm | parser

result = chain.invoke({
    "book_name": "어린왕자",
    "format_instructions": parser.get_format_instructions()
})

print(type(result))        # <class 'BookInfo'>
print(result.title)        # 어린 왕자
print(result.author)       # 앙투안 드 생텍쥐페리
print(result.year)         # 1943
print(result.genres)       # ['소설', '동화', '판타지']
