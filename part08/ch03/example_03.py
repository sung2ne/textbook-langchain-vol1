class ProductAnalyzer:
    # ... 기존 코드 ...

    def compare(self, products: list[Product]) -> dict:
        """여러 상품 비교"""
        if len(products) < 2:
            return {"error": "비교하려면 2개 이상의 상품이 필요합니다"}

        # 상품 정보 합치기
        products_text = "\n\n---\n\n".join([
            f"[상품 {i+1}]\n{p.to_text()}"
            for i, p in enumerate(products)
        ])

        prompt = ChatPromptTemplate.from_template("""
다음 상품들을 비교 분석해주세요.

{products}

다음 JSON 형식으로 응답해주세요:
{{
    "comparison_table": {{
        "항목1": {{"상품1": "값", "상품2": "값"}},
        "항목2": {{"상품1": "값", "상품2": "값"}}
    }},
    "winner": {{
        "성능": "상품 번호",
        "가성비": "상품 번호",
        "종합": "상품 번호"
    }},
    "recommendation": "종합 추천 의견"
}}

JSON만 출력하세요.
""")

        chain = prompt | self.llm | JsonOutputParser()

        try:
            result = chain.invoke({"products": products_text})
            return result
        except Exception as e:
            return {"error": str(e)}

    def compare_simple(self, products: list[Product]) -> str:
        """간단한 비교 (텍스트)"""
        products_text = "\n\n---\n\n".join([
            f"[상품 {i+1}]\n{p.to_text()}"
            for i, p in enumerate(products)
        ])

        prompt = ChatPromptTemplate.from_template("""
다음 상품들을 비교해주세요.

{products}

비교 결과를 표 형식과 함께 설명해주세요.
어떤 상품이 어떤 용도에 적합한지 추천해주세요.
""")

        chain = prompt | self.llm | StrOutputParser()
        return chain.invoke({"products": products_text})
