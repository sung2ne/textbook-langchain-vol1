import requests

API_KEY = "your_api_key"  # openweathermap.org에서 발급
city = "Seoul"

url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric&lang=kr"
response = requests.get(url)
data = response.json()

print(f"도시: {data['name']}")
print(f"온도: {data['main']['temp']}°C")
print(f"날씨: {data['weather'][0]['description']}")
