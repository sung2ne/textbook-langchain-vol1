import requests

response = requests.get("https://api.example.com/data")
data = response.json()  # JSON → Python dict
