from langchain_community.document_loaders import DirectoryLoader, TextLoader

# 특정 로더 사용
loader = DirectoryLoader(
    "./docs/",
    glob="**/*.txt",
    loader_cls=TextLoader,
    loader_kwargs={"encoding": "utf-8"}
)
