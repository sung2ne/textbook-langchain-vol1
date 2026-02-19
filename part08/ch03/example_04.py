from analyzer import ProductAnalyzer
from models import Product

# 비교할 상품들
products = [
    Product(
        name="갤럭시 S24 울트라",
        price=1650000,
        url="https://example.com/galaxy",
        specs={"디스플레이": "6.8인치", "프로세서": "Snapdragon 8 Gen 3", "RAM": "12GB"}
    ),
    Product(
        name="아이폰 15 Pro Max",
        price=1900000,
        url="https://example.com/iphone",
        specs={"디스플레이": "6.7인치", "프로세서": "A17 Pro", "RAM": "8GB"}
    ),
]

# 비교 분석
analyzer = ProductAnalyzer()
comparison = analyzer.compare(products)

print("=== 비교 결과 ===")
print(f"종합 추천: {comparison.get('recommendation')}")

winner = comparison.get("winner", {})
print(f"성능 우위: 상품 {winner.get('성능')}")
print(f"가성비 우위: 상품 {winner.get('가성비')}")
