class PriceAlert:
    def __init__(self):
        self.alerts = {}  # {url: target_price}

    def add_alert(self, url: str, target_price: int):
        self.alerts[url] = target_price

    def check_alerts(self, store: ProductStore) -> list[str]:
        notifications = []
        for product in store.get_all():
            if product.url in self.alerts:
                if product.price <= self.alerts[product.url]:
                    notifications.append(
                        f"🔔 {product.name}이 목표가 도달! "
                        f"현재 {product.price:,}원"
                    )
        return notifications
