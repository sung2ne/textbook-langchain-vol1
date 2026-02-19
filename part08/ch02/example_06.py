import requests
from bs4 import BeautifulSoup
from models import Product
from typing import Optional
import re


class ProductScraper:
    def __init__(self, use_llm: bool = False):
        self.use_llm = use_llm
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
        }

        if use_llm:
            from langchain_ollama import ChatOllama
            self.llm = ChatOllama(model="llama4")

    def fetch(self, url: str) -> Optional[str]:
        """URL에서 HTML 가져오기"""
        try:
            response = requests.get(url, headers=self.headers, timeout=10)
            response.raise_for_status()
            return response.text
        except Exception as e:
            print(f"페이지 로드 실패: {e}")
            return None

    def extract(self, html: str, url: str = "") -> Optional[Product]:
        """HTML에서 상품 정보 추출"""
        # 규칙 기반 추출
        product = self._extract_rules(html, url)

        if product and product.name and product.price > 0:
            return product

        # LLM 사용 설정시 LLM 추출 시도
        if self.use_llm:
            return self._extract_llm(html, url)

        return product

    def scrape(self, url: str) -> Optional[Product]:
        """URL에서 상품 정보 스크래핑"""
        html = self.fetch(url)
        if not html:
            return None

        return self.extract(html, url)

    def _extract_rules(self, html: str, url: str) -> Optional[Product]:
        """규칙 기반 추출"""
        soup = BeautifulSoup(html, "html.parser")

        # 상품명
        name = self._find_text(soup, [
            "h1.product-title",
            "h1.product-name",
            ".product-title h1",
            "h1",
        ])

        if not name:
            return None

        # 가격
        price_text = self._find_text(soup, [
            ".product-price",
            ".price",
            ".sale-price",
        ])
        price = self._clean_price(price_text) if price_text else 0

        # 설명
        description = self._find_text(soup, [
            ".product-description",
            ".description",
        ])
        description = description[:500] if description else ""

        # 스펙
        specs = self._extract_specs(soup)

        return Product(
            name=name,
            price=price,
            url=url,
            description=description,
            specs=specs
        )

    def _extract_llm(self, html: str, url: str) -> Optional[Product]:
        """LLM 기반 추출"""
        from langchain_core.prompts import ChatPromptTemplate
        from langchain_core.output_parsers import JsonOutputParser

        soup = BeautifulSoup(html, "html.parser")
        for tag in soup(["script", "style", "nav", "footer"]):
            tag.decompose()

        text = soup.get_text(separator="\n", strip=True)[:3000]

        prompt = ChatPromptTemplate.from_template("""
웹 페이지에서 상품 정보를 추출하세요.

내용:
{text}

JSON 형식:
{{"name": "상품명", "price": 숫자, "description": "설명", "specs": {{"key": "value"}}}}
""")

        chain = prompt | self.llm | JsonOutputParser()

        try:
            result = chain.invoke({"text": text})
            if result and result.get("name"):
                return Product(
                    name=result["name"],
                    price=result.get("price", 0),
                    url=url,
                    description=result.get("description", ""),
                    specs=result.get("specs", {})
                )
        except Exception:
            pass

        return None

    def _find_text(self, soup, selectors: list) -> Optional[str]:
        """여러 선택자로 텍스트 찾기"""
        for selector in selectors:
            elem = soup.select_one(selector)
            if elem:
                return elem.get_text(strip=True)
        return None

    def _clean_price(self, price_text: str) -> int:
        """가격 문자열을 숫자로 변환"""
        numbers = re.findall(r'\d+', price_text.replace(',', ''))
        return int(''.join(numbers)) if numbers else 0

    def _extract_specs(self, soup) -> dict:
        """스펙 테이블 추출"""
        specs = {}
        table = soup.select_one(".product-specs, .specs, table.specifications")

        if table:
            for row in table.select("tr"):
                cells = row.select("th, td")
                if len(cells) >= 2:
                    key = cells[0].get_text(strip=True)
                    value = cells[1].get_text(strip=True)
                    if key and value:
                        specs[key] = value

        return specs
