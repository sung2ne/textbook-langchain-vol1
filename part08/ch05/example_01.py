from dataclasses import dataclass, asdict
import json


@dataclass
class Product:
    name: str
    price: int
    url: str
    description: str = ""
    specs: dict = None
    pros: list = None
    cons: list = None

    def __post_init__(self):
        self.specs = self.specs or {}
        self.pros = self.pros or []
        self.cons = self.cons or []

    def to_dict(self) -> dict:
        return asdict(self)

    def to_text(self) -> str:
        text = f"상품명: {self.name}\n"
        text += f"가격: {self.price:,}원\n"
        if self.description:
            text += f"설명: {self.description}\n"
        if self.specs:
            text += "스펙:\n"
            for k, v in self.specs.items():
                text += f"  - {k}: {v}\n"
        return text

    @classmethod
    def from_dict(cls, data: dict) -> "Product":
        return cls(**data)


class ProductStore:
    def __init__(self, filepath: str = "products.json"):
        self.filepath = filepath
        self.products: list[Product] = []
        self._load()

    def _load(self):
        try:
            with open(self.filepath, "r", encoding="utf-8") as f:
                self.products = [Product.from_dict(p) for p in json.load(f)]
        except FileNotFoundError:
            self.products = []

    def _save(self):
        with open(self.filepath, "w", encoding="utf-8") as f:
            json.dump([p.to_dict() for p in self.products], f,
                      ensure_ascii=False, indent=2)

    def add(self, product: Product):
        for i, p in enumerate(self.products):
            if p.url == product.url:
                self.products[i] = product
                self._save()
                return
        self.products.append(product)
        self._save()

    def get_all(self) -> list[Product]:
        return self.products

    def remove(self, url: str) -> bool:
        for i, p in enumerate(self.products):
            if p.url == url:
                del self.products[i]
                self._save()
                return True
        return False

    def clear(self):
        self.products = []
        self._save()
