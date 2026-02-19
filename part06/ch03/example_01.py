from langchain_text_splitters import RecursiveCharacterTextSplitter

text = """
LangChain은 대규모 언어 모델(LLM)을 활용한 애플리케이션 개발을 위한 프레임워크입니다.

주요 기능으로는 프롬프트 관리, 체인 구성, 메모리 관리, 에이전트 등이 있습니다.

LangChain을 사용하면 복잡한 AI 애플리케이션을 쉽게 구축할 수 있습니다.
문서 요약, 질의응답, 챗봇 등 다양한 활용 사례가 있습니다.
"""

splitter = RecursiveCharacterTextSplitter(
    chunk_size=100,       # 청크 최대 크기 (문자 수)
    chunk_overlap=20,     # 청크 간 겹침
    length_function=len,
)

chunks = splitter.split_text(text)

for i, chunk in enumerate(chunks):
    print(f"[청크 {i+1}] ({len(chunk)}자)")
    print(chunk)
    print()
