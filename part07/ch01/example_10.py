from langchain_community.document_loaders import (
    TextLoader,
    PyPDFLoader,
    CSVLoader,
)
from pathlib import Path

def load_documents(directory: str) -> list:
    """다양한 형식의 문서 로드"""
    documents = []
    path = Path(directory)

    # 텍스트 파일
    for file in path.glob("*.txt"):
        loader = TextLoader(str(file), encoding="utf-8")
        documents.extend(loader.load())

    # PDF 파일
    for file in path.glob("*.pdf"):
        loader = PyPDFLoader(str(file))
        documents.extend(loader.load())

    # CSV 파일
    for file in path.glob("*.csv"):
        loader = CSVLoader(str(file), encoding="utf-8")
        documents.extend(loader.load())

    return documents


# 사용
docs = load_documents("./data/")
print(f"총 {len(docs)}개 문서 로드됨")
