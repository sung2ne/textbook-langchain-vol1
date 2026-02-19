import requests
from bs4 import BeautifulSoup

def extract_main_content(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    # 불필요한 요소 제거
    for tag in soup.find_all(["script", "style", "nav", "footer", "header"]):
        tag.decompose()

    # 본문 추출 (사이트마다 다름)
    main = soup.find("main") or soup.find("article") or soup.find("body")

    if main:
        # 텍스트만 추출
        text = main.get_text(separator="\n", strip=True)
        return text

    return soup.get_text(separator="\n", strip=True)


# 사용
content = extract_main_content("https://example.com")
print(content[:500])
