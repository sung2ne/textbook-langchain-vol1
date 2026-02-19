class EntityMemory:
    def __init__(self, llm):
        self.llm = llm
        self.entities = {}  # {"철수": "사용자의 이름, Python 개발자"}

    def extract_entities(self, text):
        prompt = f"""
다음 텍스트에서 중요한 엔티티(사람, 장소, 개념)를 추출하고 설명해주세요.

텍스트: {text}

형식:
엔티티명: 설명
"""
        response = self.llm.invoke(prompt)
        # 파싱 로직...
        return response.content

    def update(self, user_message, ai_response):
        # 엔티티 추출 및 업데이트
        pass

    def get_context(self):
        if not self.entities:
            return ""
        return "기억된 정보:\n" + "\n".join([
            f"- {name}: {desc}" for name, desc in self.entities.items()
        ])
