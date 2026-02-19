import requests

url = "https://api.exchangerate-api.com/v4/latest/USD"
response = requests.get(url)
data = response.json()

print(f"1 USD = {data['rates']['KRW']} KRW")
print(f"1 USD = {data['rates']['JPY']} JPY")
