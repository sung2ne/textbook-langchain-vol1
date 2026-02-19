from langchain_core.prompts import ChatPromptTemplate

def batch_analyze(products: list) -> list:
    """여러 상품 일괄 분석"""
    prompt = ChatPromptTemplate.from_template("""
상품을 분석하세요: {product}
JSON 형식: {{"summary": "요약", "pros": ["장점"], "cons": ["단점"]}}
""")

    chain = prompt | llm | JsonOutputParser()

    # 배치로 처리
    inputs = [{"product": p.to_text()} for p in products]
    results = chain.batch(inputs)

    return results


# 순차 처리보다 빠름
results = batch_analyze(products)
