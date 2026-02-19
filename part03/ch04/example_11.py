from langchain_ollama import ChatOllama
from langchain_core.output_parsers import PydanticOutputParser
from langchain_core.prompts import ChatPromptTemplate
from pydantic import BaseModel, Field

class SentimentResult(BaseModel):
    sentiment: str = Field(description="감정 (긍정/부정/중립)")
    confidence: float = Field(description="신뢰도 (0-1)")
    keywords: list[str] = Field(description="핵심 키워드")

llm = ChatOllama(model="llama4")
parser = PydanticOutputParser(pydantic_object=SentimentResult)

template = ChatPromptTemplate.from_messages([
    ("system", "텍스트의 감정을 분석하는 전문가입니다."),
    ("human", """다음 텍스트의 감정을 분석해주세요.

텍스트: {text}

{format_instructions}""")
])

chain = template | llm | parser

result = chain.invoke({
    "text": "이 제품 정말 좋아요! 배송도 빠르고 품질도 최고입니다.",
    "format_instructions": parser.get_format_instructions()
})

print(f"감정: {result.sentiment}")
print(f"신뢰도: {result.confidence}")
print(f"키워드: {result.keywords}")
