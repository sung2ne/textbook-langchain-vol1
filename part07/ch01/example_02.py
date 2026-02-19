from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader("document.pdf")
pages = loader.load()

# 페이지별로 문서가 분리됨
for i, page in enumerate(pages):
    print(f"--- 페이지 {i+1} ---")
    print(page.page_content[:200])
    print(page.metadata)  # {'source': 'document.pdf', 'page': 0}
