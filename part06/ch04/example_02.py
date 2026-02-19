from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import requests

llm = ChatOllama(model="llama4")

class WeatherAdvisorBot:
    def __init__(self):
        # 실제로는 API 키가 필요합니다
        self.weather_data = None

    def get_weather(self, city: str) -> dict:
        """날씨 정보 가져오기 (예시 데이터)"""
        # 실제로는 OpenWeatherMap API 등을 사용
        # 여기서는 예시 데이터 반환
        weather_examples = {
            "서울": {"temp": 15, "condition": "맑음", "humidity": 45},
            "부산": {"temp": 18, "condition": "흐림", "humidity": 60},
            "제주": {"temp": 20, "condition": "비", "humidity": 80},
        }
        return weather_examples.get(city, {"temp": 15, "condition": "알 수 없음", "humidity": 50})

    def get_advice(self, city: str, activity: str) -> str:
        weather = self.get_weather(city)

        prompt = ChatPromptTemplate.from_template("""
현재 {city}의 날씨 정보:
- 온도: {temp}°C
- 날씨: {condition}
- 습도: {humidity}%

사용자가 "{activity}" 활동을 하려고 합니다.

위 날씨 정보를 고려하여:
1. 이 활동이 적합한지 평가해주세요
2. 주의사항이나 팁을 알려주세요
3. 대안이 있다면 제안해주세요
""")

        chain = prompt | llm | StrOutputParser()

        return chain.invoke({
            "city": city,
            "temp": weather["temp"],
            "condition": weather["condition"],
            "humidity": weather["humidity"],
            "activity": activity
        })


# 사용
bot = WeatherAdvisorBot()

print("=== 날씨 기반 활동 추천 챗봇 ===\n")

cities = ["서울", "부산", "제주"]
print("도시를 선택하세요:", ", ".join(cities))
city = input("도시: ").strip()

print("\n어떤 활동을 계획하고 있나요?")
activity = input("활동: ").strip()

print("\n" + "=" * 50)
print(bot.get_advice(city, activity))
