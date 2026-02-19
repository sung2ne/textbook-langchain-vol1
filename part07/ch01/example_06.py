import json
from langchain_core.documents import Document

with open("data.json", "r", encoding="utf-8") as f:
    data = json.load(f)

documents = [
    Document(page_content=json.dumps(item, ensure_ascii=False))
    for item in data["items"]
]
