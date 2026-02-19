from scraper import ProductScraper, TEST_HTML_1, TEST_HTML_2, TEST_HTML_3
from models import ProductStore

# 스크래퍼 생성
scraper = ProductScraper(use_llm=False)

# 테스트 HTML에서 추출
products = []
for html, url in [
    (TEST_HTML_1, "https://example.com/galaxy"),
    (TEST_HTML_2, "https://example.com/macbook"),
    (TEST_HTML_3, "https://example.com/ipad"),
]:
    product = scraper.extract(html, url)
    if product:
        products.append(product)
        print(f"추출 성공: {product.name}")

# 저장소에 저장
store = ProductStore()
for product in products:
    store.add(product)

print(f"\n총 {len(store.get_all())}개 상품 저장")
