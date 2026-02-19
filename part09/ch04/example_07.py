def get_relevant_products(question: str, products: list, max_products: int = 3) -> list:
    """질문과 관련된 상품만 선택"""
    keywords = question.lower().split()

    scored = []
    for product in products:
        score = 0
        text = f"{product.name} {product.description}".lower()
        for kw in keywords:
            if kw in text:
                score += 1
        scored.append((score, product))

    scored.sort(key=lambda x: x[0], reverse=True)
    return [p for _, p in scored[:max_products]]


# 사용
relevant = get_relevant_products(question, all_products, max_products=3)
