from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.output_parsers import StrOutputParser
from langchain_core.chat_history import InMemoryChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory
import requests
from bs4 import BeautifulSoup
from datetime import datetime

llm = ChatOllama(model="llama4")

class SmartAssistant:
    def __init__(self):
        self.store = {}
        self.data_cache = {}

        self.prompt = ChatPromptTemplate.from_messages([
            ("system", """당신은 실시간 정보를 활용하는 스마트 어시스턴트입니다.

현재 시간: {current_time}

실시간 정보:
{realtime_data}

위 정보를 활용하여 사용자의 질문에 친절하게 답변해주세요.
정보가 없는 경우 솔직하게 말씀해주세요.
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

    def _fetch_all_data(self) -> str:
        """모든 실시간 데이터 수집"""
        data_parts = []

        # 환율
        try:
            resp = requests.get("https://api.exchangerate-api.com/v4/latest/USD", timeout=5)
            rates = resp.json()["rates"]
            data_parts.append(f"[환율] 1 USD = {rates['KRW']:.0f} KRW, {rates['JPY']:.0f} JPY, {rates['EUR']:.2f} EUR")
        except:
            data_parts.append("[환율] 정보 없음")

        # 뉴스 헤드라인
        try:
            resp = requests.get("https://news.ycombinator.com/", timeout=5)
            soup = BeautifulSoup(resp.text, "html.parser")
            titles = [span.find("a").text for span in soup.find_all("span", class_="titleline")[:5] if span.find("a")]
            news_text = "\n".join([f"  - {t}" for t in titles])
            data_parts.append(f"[기술 뉴스]\n{news_text}")
        except:
            data_parts.append("[기술 뉴스] 정보 없음")

        self.data_cache = "\n\n".join(data_parts)
        return self.data_cache

    def chat(self, message: str, session_id: str = "default") -> str:
        # 데이터 새로고침 (5분마다 또는 캐시 없을 때)
        if not self.data_cache:
            self._fetch_all_data()

        current_time = datetime.now().strftime("%Y-%m-%d %H:%M")

        config = {"configurable": {"session_id": session_id}}
        return self.chatbot.invoke(
            {
                "input": message,
                "current_time": current_time,
                "realtime_data": self.data_cache
            },
            config=config
        )

    def refresh(self):
        """데이터 새로고침"""
        self._fetch_all_data()
        return "데이터가 업데이트되었습니다."


def main():
    bot = SmartAssistant()

    print("=" * 50)
    print("     스마트 어시스턴트")
    print("=" * 50)
    print("환율, 뉴스 등 실시간 정보를 활용합니다.")
    print("명령어: /refresh - 데이터 새로고침")
    print("        /clear - 대화 초기화")
    print("        /quit - 종료")
    print("=" * 50)

    session_id = "user"

    while True:
        try:
            user_input = input("\n👤 You: ").strip()

            if not user_input:
                continue
            elif user_input == "/quit":
                print("안녕히 가세요!")
                break
            elif user_input == "/refresh":
                print(f"🔄 {bot.refresh()}")
            elif user_input == "/clear":
                bot.store[session_id] = InMemoryChatMessageHistory()
                print("🗑️ 대화가 초기화되었습니다.")
            else:
                print("\n🤖 AI: ", end="", flush=True)
                response = bot.chat(user_input, session_id)
                print(response)

        except KeyboardInterrupt:
            print("\n\n안녕히 가세요!")
            break


if __name__ == "__main__":
    main()
