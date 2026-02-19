from analyzer import ProductAnalyzer
from models import Product

# 테스트 상품
product = Product(
    name="갤럭시 S24 울트라",
    price=1650000,
    url="https://example.com/galaxy",
    description="삼성의 최신 플래그십 스마트폰",
    specs={
        "디스플레이": "6.8인치 QHD+ Dynamic AMOLED 2X",
        "프로세서": "Snapdragon 8 Gen 3",
        "RAM": "12GB",
        "배터리": "5000mAh",
        "카메라": "200MP"
    }
)

# 분석
analyzer = ProductAnalyzer()
result = analyzer.analyze(product)

print("=== 분석 결과 ===")
print(f"요약: {result.get('summary')}")
print(f"장점: {result.get('pros')}")
print(f"단점: {result.get('cons')}")
print(f"추천 대상: {result.get('target_user')}")
print(f"가성비: {result.get('value_rating')}")
