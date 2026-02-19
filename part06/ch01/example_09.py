from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import requests
from bs4 import BeautifulSoup

def get_news_titles(url="https://news.ycombinator.com/"):
    """Hacker News에서 뉴스 제목 가져오기"""
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    titles = []
    for span in soup.find_all("span", class_="titleline")[:10]:
        link = span.find("a")
        if link:
            titles.append(link.text)

    return titles


def summarize_news():
    llm = ChatOllama(model="llama4")

    prompt = ChatPromptTemplate.from_template("""
다음은 오늘의 주요 기술 뉴스 제목들입니다.

{titles}

위 뉴스들을 분석하여 다음을 답변해주세요:
1. 오늘의 주요 트렌드 (2-3개)
2. 가장 주목할 만한 뉴스와 그 이유
3. 개발자에게 영향을 줄 수 있는 소식
""")

    chain = prompt | llm | StrOutputParser()

    titles = get_news_titles()
    titles_text = "\n".join([f"- {t}" for t in titles])

    return chain.invoke({"titles": titles_text})


# 실행
print(summarize_news())
