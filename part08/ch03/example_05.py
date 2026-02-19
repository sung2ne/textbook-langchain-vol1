class ProductAnalyzer:
    # ... 기존 코드 ...

    def recommend(self, products: list[Product], requirements: str) -> dict:
        """요구사항에 맞는 상품 추천"""
        products_text = "\n\n---\n\n".join([
            f"[상품 {i+1}] {p.name}\n{p.to_text()}"
            for i, p in enumerate(products)
        ])

        prompt = ChatPromptTemplate.from_template("""
다음 상품들 중에서 사용자 요구에 맞는 상품을 추천해주세요.

상품 목록:
{products}

사용자 요구사항:
{requirements}

다음 JSON 형식으로 응답해주세요:
{{
    "recommended_index": 추천 상품 번호 (0부터 시작),
    "reason": "추천 이유",
    "match_score": 적합도 (1-10),
    "alternatives": [
        {{"index": 대안 상품 번호, "reason": "대안인 이유"}}
    ]
}}

JSON만 출력하세요.
""")

        chain = prompt | self.llm | JsonOutputParser()

        try:
            result = chain.invoke({
                "products": products_text,
                "requirements": requirements
            })

            # 추천 상품 정보 추가
            idx = result.get("recommended_index", 0)
            if 0 <= idx < len(products):
                result["recommended_product"] = products[idx].name

            return result
        except Exception as e:
            return {"error": str(e)}
