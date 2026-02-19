import asyncio
from langchain_ollama import ChatOllama

llm = ChatOllama(model="llama4")


async def async_analyze(product):
    """비동기 분석"""
    prompt = ChatPromptTemplate.from_template("상품 분석: {product}")
    chain = prompt | llm | StrOutputParser()

    result = await chain.ainvoke({"product": product.to_text()})
    return result


async def analyze_all(products: list):
    """모든 상품 동시 분석"""
    tasks = [async_analyze(p) for p in products]
    results = await asyncio.gather(*tasks)
    return results


# 실행
results = asyncio.run(analyze_all(products))
