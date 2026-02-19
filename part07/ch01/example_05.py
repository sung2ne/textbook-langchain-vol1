from langchain_community.document_loaders import JSONLoader

# JSON 구조에 따라 jq_schema 지정
loader = JSONLoader(
    file_path="data.json",
    jq_schema=".items[]",  # items 배열의 각 항목
    text_content=False
)

documents = loader.load()
