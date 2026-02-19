# JSONPlaceholder (테스트용)
response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
print(response.json())

# 공휴일 API
response = requests.get("https://date.nager.at/api/v3/PublicHolidays/2024/KR")
holidays = response.json()
for h in holidays[:3]:
    print(f"{h['date']}: {h['name']}")
