from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import requests

llm = ChatOllama(model="llama4")

def get_weather(city: str) -> dict:
    """날씨 정보 가져오기 (실제로는 API 키 필요)"""
    # 예시 데이터 (실제로는 API 호출)
    return {
        "city": city,
        "temp": 15,
        "description": "맑음",
        "humidity": 45
    }

def weather_chatbot(city: str, question: str) -> str:
    weather = get_weather(city)

    prompt = ChatPromptTemplate.from_template("""
현재 {city}의 날씨 정보입니다.
- 온도: {temp}°C
- 날씨: {description}
- 습도: {humidity}%

사용자 질문: {question}

위 날씨 정보를 바탕으로 친절하게 답변해주세요.
""")

    chain = prompt | llm | StrOutputParser()

    return chain.invoke({
        "city": weather["city"],
        "temp": weather["temp"],
        "description": weather["description"],
        "humidity": weather["humidity"],
        "question": question
    })


# 사용
print(weather_chatbot("서울", "오늘 우산 필요해?"))
print(weather_chatbot("서울", "산책하기 좋은 날씨야?"))
