from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.output_parsers import StrOutputParser
from langchain_core.chat_history import InMemoryChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory

llm = ChatOllama(model="llama4")

class DocumentChatbot:
    def __init__(self, document_text: str):
        self.document = document_text
        self.store = {}

        self.prompt = ChatPromptTemplate.from_messages([
            ("system", """당신은 문서 기반 질의응답 어시스턴트입니다.

참고 문서:
{document}

위 문서를 바탕으로 질문에 답변해주세요.
문서에 없는 내용은 "문서에서 해당 정보를 찾을 수 없습니다"라고 답변하세요.
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

    def chat(self, question: str, session_id: str = "default") -> str:
        config = {"configurable": {"session_id": session_id}}
        return self.chatbot.invoke(
            {"input": question, "document": self.document},
            config=config
        )


# 사용
document = """
# 회사 소개

ABC 주식회사는 2010년 1월 15일에 설립되었습니다.

## 주요 제품
- AI 어시스턴트 서비스
- 클라우드 인프라 솔루션
- 데이터 분석 플랫폼

## 연락처
- 대표전화: 02-1234-5678
- 이메일: contact@abc.com
"""

bot = DocumentChatbot(document)

print(bot.chat("회사 설립일이 언제야?"))
print(bot.chat("주요 제품 알려줘"))
print(bot.chat("연락처는?"))
print(bot.chat("방금 물어본 설립일이 몇 년 전이야?"))  # 맥락 유지
