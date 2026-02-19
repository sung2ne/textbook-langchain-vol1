from models import Product, ProductStore

# 상품 생성
product = Product(
    name="아이폰 15 Pro",
    price=1550000,
    url="https://example.com/iphone15",
    description="Apple의 최신 플래그십 스마트폰",
    specs={
        "디스플레이": "6.1인치 Super Retina XDR",
        "프로세서": "A17 Pro",
        "저장용량": "256GB",
        "카메라": "48MP 메인"
    }
)

# 텍스트 출력
print(product.to_text())

# 저장소 사용
store = ProductStore()
store.add(product)
print(f"저장된 상품: {len(store.get_all())}개")
