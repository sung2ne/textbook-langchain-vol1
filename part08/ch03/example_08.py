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

JSON 형식:
{{"summary": "요약", "pros": ["장점"], "cons": ["단점"], "target_user": "추천 대상", "value_rating": "상/중/하"}}
""")

        chain = prompt | self.llm | JsonOutputParser()

        try:
            return chain.invoke({"product_info": product.to_text()})
        except Exception as e:
            return {"error": str(e)}

    def summarize(self, product: Product) -> str:
        """상품 요약"""
        prompt = ChatPromptTemplate.from_template("""
상품을 한 문장으로 요약하세요.

{product_info}
""")
        chain = prompt | self.llm | StrOutputParser()
        return chain.invoke({"product_info": product.to_text()})

    def compare(self, products: list[Product]) -> dict:
        """여러 상품 비교"""
        if len(products) < 2:
            return {"error": "2개 이상 필요"}

        products_text = self._format_products(products)

        prompt = ChatPromptTemplate.from_template("""
상품들을 비교 분석하세요.

{products}

JSON 형식:
{{"comparison": "비교 요약", "winner": {{"성능": "번호", "가성비": "번호"}}, "recommendation": "추천"}}
""")

        chain = prompt | self.llm | JsonOutputParser()

        try:
            return chain.invoke({"products": products_text})
        except Exception as e:
            return {"error": str(e)}

    def compare_text(self, products: list[Product]) -> str:
        """텍스트 형식 비교"""
        products_text = self._format_products(products)

        prompt = ChatPromptTemplate.from_template("""
상품들을 비교해주세요. 표 형식으로 정리하고 추천해주세요.

{products}
""")
        chain = prompt | self.llm | StrOutputParser()
        return chain.invoke({"products": products_text})

    def recommend(self, products: list[Product], requirements: str) -> dict:
        """요구사항에 맞는 추천"""
        products_text = self._format_products(products)

        prompt = ChatPromptTemplate.from_template("""
요구사항에 맞는 상품을 추천하세요.

상품:
{products}

요구사항: {requirements}

JSON 형식:
{{"recommended_index": 번호, "reason": "이유", "match_score": 1-10}}
""")

        chain = prompt | self.llm | JsonOutputParser()

        try:
            result = chain.invoke({
                "products": products_text,
                "requirements": requirements
            })
            idx = result.get("recommended_index", 0)
            if 0 <= idx < len(products):
                result["recommended_product"] = products[idx].name
            return result
        except Exception as e:
            return {"error": str(e)}

    def ask(self, products: list[Product], question: str) -> str:
        """질문 응답"""
        products_text = self._format_products(products)

        prompt = ChatPromptTemplate.from_template("""
상품 정보를 참고하여 답변하세요.

{products}

질문: {question}

정보가 없으면 "해당 정보가 없습니다"라고 답변하세요.
""")

        chain = prompt | self.llm | StrOutputParser()
        return chain.invoke({
            "products": products_text,
            "question": question
        })

    def _format_products(self, products: list[Product]) -> str:
        """상품 목록 포맷팅"""
        return "\n\n---\n\n".join([
            f"[상품 {i+1}] {p.name}\n{p.to_text()}"
            for i, p in enumerate(products)
        ])
