from langchain_text_splitters import RecursiveCharacterTextSplitter

# 문서 분할
splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)
chunks = splitter.split_documents(documents)

# 각 청크에서 관련 내용 찾기
def find_relevant_chunks(question: str, chunks: list, top_k: int = 3) -> list:
    """간단한 키워드 기반 관련성 검색"""
    keywords = question.lower().split()

    scored_chunks = []
    for chunk in chunks:
        content_lower = chunk.page_content.lower()
        score = sum(1 for kw in keywords if kw in content_lower)
        scored_chunks.append((score, chunk))

    # 점수순 정렬
    scored_chunks.sort(key=lambda x: x[0], reverse=True)

    return [chunk for score, chunk in scored_chunks[:top_k] if score > 0]


# 사용
relevant = find_relevant_chunks("설립일", chunks)
context = "\n\n".join([c.page_content for c in relevant])

response = chain.invoke({
    "document": context,
    "question": "회사 설립일은 언제인가요?"
})
