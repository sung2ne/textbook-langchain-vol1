from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

llm = ChatOllama(model="llama4")

# 감정 분석 체인
sentiment_prompt = ChatPromptTemplate.from_template(
    "다음 텍스트의 감정을 '긍정', '부정', '중립' 중 하나로 답해주세요: {text}"
)
sentiment_chain = sentiment_prompt | llm | StrOutputParser()

# 키워드 추출 체인
keyword_prompt = ChatPromptTemplate.from_template(
    "다음 텍스트의 핵심 키워드 3개를 쉼표로 구분해서 답해주세요: {text}"
)
keyword_chain = keyword_prompt | llm | StrOutputParser()

# 병렬 실행
analysis_chain = {
    "sentiment": sentiment_chain,
    "keywords": keyword_chain,
    "original": RunnablePassthrough()  # 원본 유지
}

result = analysis_chain.invoke({"text": "이 제품 정말 좋아요! 배송도 빠르고 품질도 최고입니다."})
print(result)
