from langchain_community.document_loaders import TextLoader

loader = TextLoader("example.txt")
documents = loader.load()

# 메타데이터 확인
print(documents[0].metadata)
# {'source': 'example.txt'}

# 메타데이터 추가
documents[0].metadata["author"] = "홍길동"
documents[0].metadata["date"] = "2024-01-01"
