from langchain_core.documents import Document

doc = Document(
    page_content="LangChain은 AI 프레임워크입니다.",
    metadata={
        "source": "https://example.com",
        "author": "LangChain Team",
        "date": "2024-01-01"
    }
)

print(doc.page_content)
print(doc.metadata)
