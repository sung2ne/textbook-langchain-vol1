from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader("document.pdf")
pages = loader.load()

# 모든 페이지 합치기
full_text = "\n".join([p.page_content for p in pages])
