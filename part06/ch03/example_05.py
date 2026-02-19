from langchain_community.document_loaders import WebBaseLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

# 1. 웹 페이지 로드
loader = WebBaseLoader("https://example.com/article")
documents = loader.load()

# 2. 문서 분할
splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)
chunks = splitter.split_documents(documents)

print(f"원본 문서: {len(documents)}개")
print(f"분할된 청크: {len(chunks)}개")

# 3. 각 청크 처리
for chunk in chunks:
    print(f"[{chunk.metadata['source']}]")
    print(chunk.page_content[:100], "...")
    print()
