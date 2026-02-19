from langchain_community.document_loaders import WebBaseLoader

loader = WebBaseLoader("https://example.com")
documents = loader.load()

print(documents[0].page_content[:500])
print(documents[0].metadata)
