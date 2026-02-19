from analyzer import ProductAnalyzer
from models import ProductStore

# 저장된 상품 불러오기
store = ProductStore()
products = store.get_all()

if products:
    analyzer = ProductAnalyzer()

    # 모든 상품 요약
    print("=== 상품 요약 ===")
    for p in products:
        summary = analyzer.summarize(p)
        print(f"- {p.name}: {summary}")

    # 비교 분석
    if len(products) >= 2:
        print("\n=== 비교 분석 ===")
        comparison = analyzer.compare_text(products)
        print(comparison)

    # 질문 응답
    print("\n=== Q&A ===")
    questions = [
        "가장 화면이 큰 제품은?",
        "배터리가 가장 오래가는 제품은?",
        "가장 가격이 저렴한 제품은?",
    ]

    for q in questions:
        answer = analyzer.ask(products, q)
        print(f"Q: {q}")
        print(f"A: {answer}\n")
