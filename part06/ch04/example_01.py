from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.output_parsers import StrOutputParser
from langchain_core.chat_history import InMemoryChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory
import requests
from bs4 import BeautifulSoup

llm = ChatOllama(model="llama4")

class NewsBriefingBot:
    def __init__(self):
        self.store = {}
        self.news_cache = None

        self.prompt = ChatPromptTemplate.from_messages([
            ("system", """당신은 뉴스 브리핑 전문가입니다.

오늘의 뉴스:
{news}

위 뉴스 정보를 바탕으로 사용자의 질문에 답변해주세요.
뉴스에 없는 내용은 "해당 정보는 오늘 뉴스에 없습니다"라고 답변하세요.
"""),
            MessagesPlaceholder(variable_name="history"),
            ("human", "{input}")
        ])

        self.chain = self.prompt | llm | StrOutputParser()

        self.chatbot = RunnableWithMessageHistory(
            self.chain,
            self._get_history,
            input_messages_key="input",
            history_messages_key="history"
        )

    def _get_history(self, session_id: str):
        if session_id not in self.store:
            self.store[session_id] = InMemoryChatMessageHistory()
        return self.store[session_id]

    def fetch_news(self) -> str:
        """Hacker News에서 뉴스 가져오기"""
        try:
            response = requests.get("https://news.ycombinator.com/", timeout=10)
            soup = BeautifulSoup(response.text, "html.parser")

            news_items = []
            for span in soup.find_all("span", class_="titleline")[:10]:
                link = span.find("a")
                if link:
                    news_items.append(f"- {link.text}")

            self.news_cache = "\n".join(news_items)
            return self.news_cache
        except Exception as e:
            return f"뉴스를 가져오는데 실패했습니다: {e}"

    def chat(self, message: str, session_id: str = "default") -> str:
        # 뉴스 캐시 확인
        if self.news_cache is None:
            self.fetch_news()

        config = {"configurable": {"session_id": session_id}}
        return self.chatbot.invoke(
            {"input": message, "news": self.news_cache},
            config=config
        )

    def refresh_news(self):
        """뉴스 새로고침"""
        self.fetch_news()
        return "뉴스가 업데이트되었습니다."


# 사용
bot = NewsBriefingBot()

print("=== 뉴스 브리핑 챗봇 ===")
print("명령어: /refresh - 뉴스 새로고침, /quit - 종료\n")

while True:
    user_input = input("You: ").strip()

    if user_input == "/quit":
        break
    elif user_input == "/refresh":
        print(f"Bot: {bot.refresh_news()}\n")
    else:
        response = bot.chat(user_input)
        print(f"Bot: {response}\n")
