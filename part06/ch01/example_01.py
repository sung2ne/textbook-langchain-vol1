import requests

# GET 요청
response = requests.get("https://example.com")

print(response.status_code)  # 200
print(response.text[:500])   # HTML 내용
