from langchain_community.document_loaders import DirectoryLoader

# 모든 txt 파일 로드
loader = DirectoryLoader("./docs/", glob="**/*.txt", show_progress=True)
documents = loader.load()

print(f"로드된 문서: {len(documents)}개")
