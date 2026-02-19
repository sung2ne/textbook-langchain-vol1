import requests
from bs4 import BeautifulSoup
from models import Product
from typing import Optional
import re


def clean_price(price_text: str) -> int:
    """가격 문자열을 숫자로 변환"""
    # 숫자만 추출
    numbers = re.findall(r'\d+', price_text.replace(',', ''))
    if numbers:
        return int(''.join(numbers))
    return 0


def extract_from_html(html: str, url: str = "") -> Optional[Product]:
    """HTML에서 상품 정보 추출"""
    soup = BeautifulSoup(html, "html.parser")

    # 상품명 추출 (여러 패턴 시도)
    name = None
    name_selectors = [
        "h1.product-title",
        "h1.product-name",
        ".product-title h1",
        "h1[itemprop='name']",
        "h1",
    ]

    for selector in name_selectors:
        elem = soup.select_one(selector)
        if elem:
            name = elem.get_text(strip=True)
            break

    if not name:
        return None

    # 가격 추출
    price = 0
    price_selectors = [
        ".product-price",
        ".price",
        "[itemprop='price']",
        ".sale-price",
    ]

    for selector in price_selectors:
        elem = soup.select_one(selector)
        if elem:
            price = clean_price(elem.get_text())
            break

    # 설명 추출
    description = ""
    desc_selectors = [
        ".product-description",
        ".description",
        "[itemprop='description']",
    ]

    for selector in desc_selectors:
        elem = soup.select_one(selector)
        if elem:
            description = elem.get_text(strip=True)[:500]  # 최대 500자
            break

    # 스펙 추출 (테이블 형태)
    specs = {}
    spec_table = soup.select_one(".product-specs, .specs, table.specifications")

    if spec_table:
        rows = spec_table.select("tr")
        for row in rows:
            cells = row.select("th, td")
            if len(cells) >= 2:
                key = cells[0].get_text(strip=True)
                value = cells[1].get_text(strip=True)
                if key and value:
                    specs[key] = value

    return Product(
        name=name,
        price=price,
        url=url,
        description=description,
        specs=specs
    )


def fetch_product(url: str) -> Optional[Product]:
    """URL에서 상품 정보 가져오기"""
    try:
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
        }
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()

        return extract_from_html(response.text, url)
    except Exception as e:
        print(f"스크래핑 실패: {e}")
        return None
