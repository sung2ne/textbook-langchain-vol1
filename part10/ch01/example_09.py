import requests
from bs4 import BeautifulSoup

response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
content = soup.select_one("article").get_text()
