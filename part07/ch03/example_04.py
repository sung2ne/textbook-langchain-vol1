from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.output_parsers import StrOutputParser
from langchain_core.chat_history import InMemoryChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory
import pandas as pd

llm = ChatOllama(model="llama4")

class DataAnalystBot:
    def __init__(self, csv_path: str):
        self.df = pd.read_csv(csv_path)
        self.summary = self._generate_summary()
        self.store = {}

        self.prompt = ChatPromptTemplate.from_messages([
            ("system", """당신은 데이터 분석 전문가입니다.

데이터 요약:
{summary}

실제 데이터:
{data}

위 데이터를 분석하여 질문에 답변해주세요.
숫자가 필요한 경우 정확하게 계산해주세요.
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

    def _generate_summary(self) -> str:
        lines = [
            f"컬럼: {', '.join(self.df.columns.tolist())}",
            f"총 레코드: {len(self.df)}개"
        ]
        return "\n".join(lines)

    def _get_history(self, session_id: str):
        if session_id not in self.store:
            self.store[session_id] = InMemoryChatMessageHistory()
        return self.store[session_id]

    def chat(self, question: str, session_id: str = "default") -> str:
        config = {"configurable": {"session_id": session_id}}
        return self.chatbot.invoke({
            "input": question,
            "summary": self.summary,
            "data": self.df.to_string(index=False)
        }, config=config)

    def filter(self, column: str, value) -> pd.DataFrame:
        """데이터 필터링"""
        return self.df[self.df[column] == value]

    def top_n(self, column: str, n: int = 5) -> pd.DataFrame:
        """상위 N개"""
        return self.df.nlargest(n, column)


# 사용
bot = DataAnalystBot("products.csv")

print(bot.chat("가장 비싼 상품 3개 알려줘"))
print(bot.chat("전자기기의 총 재고는 얼마야?"))
print(bot.chat("가구 카테고리 상품들 알려줘"))
