from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.output_parsers import StrOutputParser
from langchain_core.chat_history import InMemoryChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_community.document_loaders import DirectoryLoader, TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from pathlib import Path

class KnowledgeBase:
    def __init__(self, directory: str, chunk_size: int = 500):
        self.directory = directory
        self.documents = []
        self.chunks = []
        self.store = {}

        self._load_documents()
        self._split_documents(chunk_size)
        self._setup_chain()

    def _load_documents(self):
        """디렉토리에서 모든 문서 로드"""
        path = Path(self.directory)

        for txt_file in path.rglob("*.txt"):
            try:
                loader = TextLoader(str(txt_file), encoding="utf-8")
                docs = loader.load()
                # 카테고리 메타데이터 추가
                category = txt_file.parent.name
                for doc in docs:
                    doc.metadata["category"] = category
                self.documents.extend(docs)
            except Exception as e:
                print(f"로드 실패: {txt_file} - {e}")

        print(f"총 {len(self.documents)}개 문서 로드됨")

    def _split_documents(self, chunk_size: int):
        """문서 분할"""
        splitter = RecursiveCharacterTextSplitter(
            chunk_size=chunk_size,
            chunk_overlap=50
        )
        self.chunks = splitter.split_documents(self.documents)
        print(f"총 {len(self.chunks)}개 청크 생성됨")

    def _setup_chain(self):
        """LLM 체인 설정"""
        self.llm = ChatOllama(model="llama4")

        self.prompt = ChatPromptTemplate.from_messages([
            ("system", """당신은 회사의 지식 베이스를 기반으로 답변하는 어시스턴트입니다.

관련 문서:
{context}

위 문서들을 참고하여 질문에 답변해주세요.
답변 시 어느 문서에서 정보를 찾았는지 출처를 밝혀주세요.
문서에 없는 내용은 "지식 베이스에서 해당 정보를 찾을 수 없습니다"라고 답변하세요.
"""),
            MessagesPlaceholder(variable_name="history"),
            ("human", "{input}")
        ])

        self.chain = self.prompt | self.llm | StrOutputParser()
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

    def search(self, query: str, top_k: int = 3) -> list:
        """키워드 기반 검색"""
        keywords = query.lower().split()

        scored = []
        for chunk in self.chunks:
            content = chunk.page_content.lower()
            score = sum(1 for kw in keywords if kw in content)
            if score > 0:
                scored.append((score, chunk))

        scored.sort(key=lambda x: x[0], reverse=True)
        return [chunk for _, chunk in scored[:top_k]]

    def ask(self, question: str, session_id: str = "default") -> str:
        """질문에 답변"""
        # 관련 문서 검색
        relevant = self.search(question)

        if not relevant:
            return "관련 문서를 찾을 수 없습니다."

        # 컨텍스트 구성
        context_parts = []
        for chunk in relevant:
            source = chunk.metadata.get("source", "unknown")
            category = chunk.metadata.get("category", "general")
            context_parts.append(f"[{category}/{source}]\n{chunk.page_content}")

        context = "\n\n---\n\n".join(context_parts)

        config = {"configurable": {"session_id": session_id}}
        return self.chatbot.invoke(
            {"input": question, "context": context},
            config=config
        )

    def list_documents(self) -> list:
        """문서 목록"""
        return [doc.metadata.get("source") for doc in self.documents]

    def get_stats(self) -> dict:
        """통계"""
        categories = {}
        for doc in self.documents:
            cat = doc.metadata.get("category", "general")
            categories[cat] = categories.get(cat, 0) + 1

        return {
            "total_documents": len(self.documents),
            "total_chunks": len(self.chunks),
            "categories": categories
        }


# 사용
kb = KnowledgeBase("./knowledge_base/")
print(kb.get_stats())

print(kb.ask("회사 소개해줘"))
print(kb.ask("개인정보 처리 방침은?"))
