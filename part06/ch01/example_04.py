import requests
from bs4 import BeautifulSoup

url = "https://news.ycombinator.com/"  # Hacker News

response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# 뉴스 제목 추출
titles = soup.find_all("span", class_="titleline")
for i, title in enumerate(titles[:5], 1):
    link = title.find("a")
    if link:
        print(f"{i}. {link.text}")
