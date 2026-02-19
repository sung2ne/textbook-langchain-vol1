from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.documents import Document

doc = Document(
    page_content="긴 텍스트...",
    metadata={"source": "web"}
)

splitter = RecursiveCharacterTextSplitter(chunk_size=100, chunk_overlap=20)

# 문서 분할 (메타데이터 유지)
chunks = splitter.split_documents([doc])

for chunk in chunks:
    print(chunk.metadata)  # 원본 메타데이터 유지됨
