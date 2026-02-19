from scraper import extract_from_html, TEST_HTML_1, TEST_HTML_2, TEST_HTML_3
from models import ProductStore

# 테스트 HTML에서 상품 정보 추출
product1 = extract_from_html(TEST_HTML_1, "https://example.com/galaxy-s24")
product2 = extract_from_html(TEST_HTML_2, "https://example.com/macbook-pro")
product3 = extract_from_html(TEST_HTML_3, "https://example.com/ipad-pro")

# 출력
for product in [product1, product2, product3]:
    if product:
        print(product.to_text())
        print("-" * 40)

# 저장소에 추가
store = ProductStore()
for product in [product1, product2, product3]:
    if product:
        store.add(product)

print(f"\n총 {len(store.get_all())}개 상품 저장됨")
