from langchain_community.document_loaders import (
    TextLoader,
    PyPDFLoader,
    CSVLoader,
    DirectoryLoader,
)

loader = TextLoader("file.txt", encoding="utf-8")
documents = loader.load()
