from langchain_community.document_loaders.csv_loader import CSVLoader

loader = CSVLoader("data.csv", encoding="utf-8")
documents = loader.load()

for doc in documents[:3]:
    print(doc.page_content)
    print("---")
