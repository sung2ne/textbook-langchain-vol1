from datetime import datetime


class PriceHistory:
    def __init__(self, filepath: str = "price_history.json"):
        self.filepath = filepath
        self.history = {}  # {url: [(date, price), ...]}
        self._load()

    def record(self, product: Product):
        url = product.url
        if url not in self.history:
            self.history[url] = []
        self.history[url].append({
            "date": datetime.now().isoformat(),
            "price": product.price
        })
        self._save()

    def get_trend(self, url: str) -> str:
        if url not in self.history or len(self.history[url]) < 2:
            return "데이터 부족"

        prices = [h["price"] for h in self.history[url]]
        if prices[-1] < prices[0]:
            return f"📉 하락 ({prices[0]:,} → {prices[-1]:,})"
        elif prices[-1] > prices[0]:
            return f"📈 상승 ({prices[0]:,} → {prices[-1]:,})"
        else:
            return "➡️ 유지"
