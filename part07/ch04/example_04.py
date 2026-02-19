class KnowledgeBase:
    # ... 기존 코드 ...

    def add_document(self, filepath: str, category: str = "general"):
        """새 문서 추가"""
        try:
            loader = TextLoader(filepath, encoding="utf-8")
            docs = loader.load()

            for doc in docs:
                doc.metadata["category"] = category

            self.documents.extend(docs)

            # 청크 재생성
            splitter = RecursiveCharacterTextSplitter(
                chunk_size=500,
                chunk_overlap=50
            )
            new_chunks = splitter.split_documents(docs)
            self.chunks.extend(new_chunks)

            print(f"문서 추가됨: {filepath}")
        except Exception as e:
            print(f"추가 실패: {e}")

    def refresh(self):
        """지식 베이스 새로고침"""
        self.documents = []
        self.chunks = []
        self._load_documents()
        self._split_documents(500)
        print("지식 베이스 새로고침 완료")
