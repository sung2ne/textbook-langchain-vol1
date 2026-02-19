from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableLambda, RunnableParallel
import requests

llm = ChatOllama(model="llama4")

class IntegratedAssistant:
    def __init__(self):
        pass

    def get_exchange_rate(self, _) -> str:
        """환율 정보"""
        try:
            response = requests.get(
                "https://api.exchangerate-api.com/v4/latest/USD",
                timeout=5
            )
            data = response.json()
            krw = data["rates"]["KRW"]
            jpy = data["rates"]["JPY"]
            return f"1 USD = {krw:.0f} KRW, {jpy:.0f} JPY"
        except:
            return "환율 정보를 가져올 수 없습니다."

    def get_holidays(self, _) -> str:
        """공휴일 정보"""
        try:
            response = requests.get(
                "https://date.nager.at/api/v3/PublicHolidays/2024/KR",
                timeout=5
            )
            holidays = response.json()[:3]
            return "\n".join([f"- {h['date']}: {h['name']}" for h in holidays])
        except:
            return "공휴일 정보를 가져올 수 없습니다."

    def answer(self, question: str) -> str:
        # 병렬로 정보 수집
        info_chain = RunnableParallel(
            exchange=RunnableLambda(self.get_exchange_rate),
            holidays=RunnableLambda(self.get_holidays),
            question=RunnableLambda(lambda x: x)
        )

        prompt = ChatPromptTemplate.from_template("""
사용 가능한 실시간 정보:

[환율 정보]
{exchange}

[한국 공휴일]
{holidays}

사용자 질문: {question}

위 정보를 활용하여 질문에 답변해주세요.
정보가 없는 질문에는 "해당 정보는 현재 제공되지 않습니다"라고 답변하세요.
""")

        chain = info_chain | prompt | llm | StrOutputParser()
        return chain.invoke(question)


# 사용
assistant = IntegratedAssistant()

print("=== 정보 통합 어시스턴트 ===")
print("환율, 공휴일 관련 질문에 답변합니다.\n")

questions = [
    "1000달러는 얼마야?",
    "올해 공휴일 알려줘",
    "일본 여행 가려면 엔화로 얼마나 환전해야 해?"
]

for q in questions:
    print(f"Q: {q}")
    print(f"A: {assistant.answer(q)}\n")
