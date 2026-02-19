class ProductChatbot:
    # ... 기존 코드 ...

    def add_test_products(self):
        """테스트용 상품 추가"""
        test_products = [
            Product(
                name="갤럭시 S24 울트라 256GB",
                price=1650000,
                url="https://example.com/galaxy-s24",
                description="삼성 최신 플래그십",
                specs={
                    "디스플레이": "6.8인치 QHD+",
                    "프로세서": "Snapdragon 8 Gen 3",
                    "RAM": "12GB",
                    "배터리": "5000mAh",
                }
            ),
            Product(
                name="아이폰 15 Pro Max 256GB",
                price=1900000,
                url="https://example.com/iphone-15",
                description="Apple 최신 플래그십",
                specs={
                    "디스플레이": "6.7인치 Super Retina XDR",
                    "프로세서": "A17 Pro",
                    "RAM": "8GB",
                    "배터리": "4422mAh",
                }
            ),
            Product(
                name="픽셀 8 Pro 128GB",
                price=1100000,
                url="https://example.com/pixel-8",
                description="Google AI 스마트폰",
                specs={
                    "디스플레이": "6.7인치 LTPO OLED",
                    "프로세서": "Tensor G3",
                    "RAM": "12GB",
                    "배터리": "5050mAh",
                }
            ),
        ]

        for product in test_products:
            self.store.add(product)

        return f"✅ {len(test_products)}개 테스트 상품 추가됨"
