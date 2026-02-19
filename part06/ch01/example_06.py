urls = [
    "https://example.com/page1",
    "https://example.com/page2",
]

loader = WebBaseLoader(urls)
documents = loader.load()

for doc in documents:
    print(f"URL: {doc.metadata['source']}")
    print(f"내용: {doc.page_content[:200]}...\n")
