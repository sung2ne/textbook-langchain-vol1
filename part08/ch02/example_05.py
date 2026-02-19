def smart_extract(html: str, url: str = "") -> Optional[Product]:
    """규칙 기반 → LLM 순으로 시도"""

    # 1. 먼저 규칙 기반 추출 시도
    product = extract_from_html(html, url)

    if product and product.name and product.price > 0:
        print("규칙 기반 추출 성공")
        return product

    # 2. 실패하면 LLM 사용
    print("LLM 기반 추출 시도...")
    product = extract_with_llm(html, url)

    if product:
        print("LLM 기반 추출 성공")
        return product

    print("추출 실패")
    return None
