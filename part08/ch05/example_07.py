class MultiUserChatbot:
    def __init__(self):
        self.user_stores = {}  # {user_id: ProductStore}
        self.user_histories = {}

    def get_store(self, user_id: str) -> ProductStore:
        if user_id not in self.user_stores:
            self.user_stores[user_id] = ProductStore(f"products_{user_id}.json")
        return self.user_stores[user_id]

    def process(self, user_input: str, user_id: str) -> str:
        store = self.get_store(user_id)
        # ... 처리 로직
