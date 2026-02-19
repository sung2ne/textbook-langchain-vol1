# 2권에서 배울 내용 미리보기
from langchain_community.vectorstores import Chroma

# 문서를 벡터로 변환하여 저장
vectorstore = Chroma.from_documents(
    documents=chunks,
    embedding=embeddings,
    persist_directory="./chroma_db"
)

# 유사한 문서 검색
results = vectorstore.similarity_search("LangChain 사용법", k=3)
