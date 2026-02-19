from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import requests

llm = ChatOllama(model="llama4")

def get_exchange_rate():
    """환율 정보"""
    response = requests.get("https://api.exchangerate-api.com/v4/latest/USD")
    return response.json()["rates"]

def get_holidays(year: int, country: str):
    """공휴일 정보"""
    response = requests.get(f"https://date.nager.at/api/v3/PublicHolidays/{year}/{country}")
    return response.json()

def travel_advisor(destination: str, budget_usd: float):
    """여행 조언 봇"""

    # 환율 정보
    rates = get_exchange_rate()

    # 목적지에 따른 환율
    currency_map = {"일본": "JPY", "유럽": "EUR", "영국": "GBP"}
    currency = currency_map.get(destination, "EUR")
    rate = rates.get(currency, 1)

    # 공휴일 정보
    country_map = {"일본": "JP", "독일": "DE", "영국": "GB"}
    country_code = country_map.get(destination, "DE")

    try:
        holidays = get_holidays(2024, country_code)[:5]
        holiday_text = "\n".join([f"- {h['date']}: {h['name']}" for h in holidays])
    except:
        holiday_text = "정보 없음"

    prompt = ChatPromptTemplate.from_template("""
여행 정보:
- 목적지: {destination}
- 예산: ${budget_usd} (약 {local_budget:.0f} {currency})
- 현재 환율: 1 USD = {rate:.2f} {currency}

다가오는 공휴일:
{holidays}

위 정보를 바탕으로 여행 계획 조언을 해주세요.
- 예산으로 할 수 있는 활동
- 공휴일을 고려한 일정
- 유용한 팁
""")

    chain = prompt | llm | StrOutputParser()

    return chain.invoke({
        "destination": destination,
        "budget_usd": budget_usd,
        "local_budget": budget_usd * rate,
        "currency": currency,
        "rate": rate,
        "holidays": holiday_text
    })


# 사용
print(travel_advisor("일본", 1000))
