from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.output_parsers import StrOutputParser
from langchain_core.chat_history import InMemoryChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory

from models import Product, ProductStore
from scraper import ProductScraper
from analyzer import ProductAnalyzer


class ProductChatbot:
    def __init__(self):
        self.store = ProductStore()
        self.scraper = ProductScraper(use_llm=False)
        self.analyzer = ProductAnalyzer()
        self.history_store = {}

        self._setup_chain()

    def _setup_chain(self):
        """대화 체인 설정"""
        llm = ChatOllama(model="llama4")

        self.prompt = ChatPromptTemplate.from_messages([
            ("system", """당신은 상품 비교 전문가 어시스턴트입니다.

현재 등록된 상품:
{products}

사용자의 질문에 위 상품 정보를 바탕으로 답변해주세요.
상품 비교, 추천, 스펙 설명 등을 도와드립니다.

등록된 상품이 없으면 먼저 상품을 추가하라고 안내해주세요.
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
        if session_id not in self.history_store:
            self.history_store[session_id] = InMemoryChatMessageHistory()
        return self.history_store[session_id]

    def _format_products(self) -> str:
        """상품 목록 포맷팅"""
        products = self.store.get_all()
        if not products:
            return "등록된 상품이 없습니다."

        lines = []
        for i, p in enumerate(products, 1):
            lines.append(f"{i}. {p.name} - {p.price:,}원")
            if p.specs:
                specs = ", ".join(f"{k}: {v}" for k, v in list(p.specs.items())[:3])
                lines.append(f"   스펙: {specs}")

        return "\n".join(lines)

    def chat(self, message: str, session_id: str = "default") -> str:
        """대화 처리"""
        config = {"configurable": {"session_id": session_id}}
        return self.chatbot.invoke({
            "input": message,
            "products": self._format_products()
        }, config=config)
