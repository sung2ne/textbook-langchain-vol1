from langchain_core.documents import Document
from typing import List

class MyCustomLoader:
    def __init__(self, file_path: str):
        self.file_path = file_path

    def load(self) -> List[Document]:
        documents = []

        with open(self.file_path, "r", encoding="utf-8") as f:
            # 커스텀 파싱 로직
            content = f.read()

            # 예: 구분자로 분리
            sections = content.split("===")

            for i, section in enumerate(sections):
                if section.strip():
                    documents.append(Document(
                        page_content=section.strip(),
                        metadata={
                            "source": self.file_path,
                            "section": i
                        }
                    ))

        return documents


# 사용
loader = MyCustomLoader("custom_format.txt")
docs = loader.load()
