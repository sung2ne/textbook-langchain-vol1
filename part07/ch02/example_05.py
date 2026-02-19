from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

llm = ChatOllama(model="llama4")

def qa_with_sources(question: str, documents: list) -> dict:
    # 문서 준비 (번호 부여)
    numbered_docs = []
    for i, doc in enumerate(documents, 1):
        source = doc.metadata.get("source", "unknown")
        numbered_docs.append(f"[{i}] ({source})\n{doc.page_content}")

    context = "\n\n".join(numbered_docs)

    prompt = ChatPromptTemplate.from_template("""
다음 문서들을 참고하여 질문에 답변해주세요.

문서들:
{context}

질문: {question}

다음 형식으로 답변해주세요:
답변: (질문에 대한 답변)
출처: (참고한 문서 번호들, 예: [1], [3])
""")

    chain = prompt | llm | StrOutputParser()
    response = chain.invoke({"context": context, "question": question})

    # 응답 파싱
    lines = response.strip().split("\n")
    answer = ""
    sources = ""

    for line in lines:
        if line.startswith("답변:"):
            answer = line.replace("답변:", "").strip()
        elif line.startswith("출처:"):
            sources = line.replace("출처:", "").strip()

    return {
        "answer": answer,
        "sources": sources,
        "raw_response": response
    }


# 사용
result = qa_with_sources("회사 제품은?", documents)
print(f"답변: {result['answer']}")
print(f"출처: {result['sources']}")
