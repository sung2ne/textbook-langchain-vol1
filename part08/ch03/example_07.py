class ProductAnalyzer:
    # ... 기존 코드 ...

    def ask(self, products: list[Product], question: str) -> str:
        """상품에 대한 질문 응답"""
        products_text = "\n\n---\n\n".join([
            f"[{p.name}]\n{p.to_text()}"
            for p in products
        ])

        prompt = ChatPromptTemplate.from_template("""
다음 상품 정보를 참고하여 질문에 답변해주세요.

상품 정보:
{products}

질문: {question}

상품 정보에 없는 내용은 추측하지 말고 "해당 정보가 없습니다"라고 답변하세요.
""")

        chain = prompt | self.llm | StrOutputParser()
        return chain.invoke({
            "products": products_text,
            "question": question
        })
