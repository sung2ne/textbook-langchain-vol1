from dataclasses import dataclass, asdict
from typing import Optional
import json


@dataclass
class Product:
    """상품 정보 데이터 클래스"""
    name: str
    price: int
    url: str
    description: str = ""
    specs: dict = None
    pros: list = None
    cons: list = None

    def __post_init__(self):
        if self.specs is None:
            self.specs = {}
        if self.pros is None:
            self.pros = []
        if self.cons is None:
            self.cons = []

    def to_dict(self) -> dict:
        return asdict(self)

    def to_text(self) -> str:
        """LLM에 전달할 텍스트 형식"""
        text = f"상품명: {self.name}\n"
        text += f"가격: {self.price:,}원\n"
        text += f"URL: {self.url}\n"

        if self.description:
            text += f"설명: {self.description}\n"

        if self.specs:
            text += "스펙:\n"
            for key, value in self.specs.items():
                text += f"  - {key}: {value}\n"

        return text

    @classmethod
    def from_dict(cls, data: dict) -> "Product":
        return cls(**data)


class ProductStore:
    """상품 저장소"""

    def __init__(self, filepath: str = "products.json"):
        self.filepath = filepath
        self.products: list[Product] = []
        self._load()

    def _load(self):
        """파일에서 로드"""
        try:
            with open(self.filepath, "r", encoding="utf-8") as f:
                data = json.load(f)
                self.products = [Product.from_dict(p) for p in data]
        except FileNotFoundError:
            self.products = []

    def _save(self):
        """파일에 저장"""
        with open(self.filepath, "w", encoding="utf-8") as f:
            json.dump([p.to_dict() for p in self.products], f,
                      ensure_ascii=False, indent=2)

    def add(self, product: Product):
        """상품 추가"""
        # 중복 체크 (URL 기준)
        for i, p in enumerate(self.products):
            if p.url == product.url:
                self.products[i] = product  # 업데이트
                self._save()
                return

        self.products.append(product)
        self._save()

    def get_all(self) -> list[Product]:
        """모든 상품 조회"""
        return self.products

    def get_by_name(self, keyword: str) -> list[Product]:
        """이름으로 검색"""
        keyword = keyword.lower()
        return [p for p in self.products if keyword in p.name.lower()]

    def remove(self, url: str) -> bool:
        """상품 삭제"""
        for i, p in enumerate(self.products):
            if p.url == url:
                del self.products[i]
                self._save()
                return True
        return False

    def clear(self):
        """전체 삭제"""
        self.products = []
        self._save()
