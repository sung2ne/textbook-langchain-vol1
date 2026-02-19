from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser, JsonOutputParser
from models import Product
from typing import Optional


class ProductAnalyzer:
    def __init__(self):
        self.llm = ChatOllama(model="llama4")

    def analyze(self, product: Product) -> dict:
        """단일 상품 분석"""
        prompt = ChatPromptTemplate.from_template("""
다음 상품을 분석해주세요.

{product_info}

다음 JSON 형식으로 응답해주세요:
{{
    "summary": "상품 요약 (50자 이내)",
    "pros": ["장점1", "장점2", "장점3"],
    "cons": ["단점1", "단점2"],
    "target_user": "추천 대상",
    "value_rating": "가성비 평가 (상/중/하)"
}}

JSON만 출력하세요.
""")

        chain = prompt | self.llm | JsonOutputParser()

        try:
            result = chain.invoke({"product_info": product.to_text()})
            return result
        except Exception as e:
            return {"error": str(e)}

    def summarize(self, product: Product) -> str:
        """상품 요약"""
        prompt = ChatPromptTemplate.from_template("""
다음 상품을 한 문장으로 요약해주세요.

{product_info}

요약:
""")

        chain = prompt | self.llm | StrOutputParser()
        return chain.invoke({"product_info": product.to_text()})
