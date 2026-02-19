from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.document_loaders import DirectoryLoader, TextLoader

llm = ChatOllama(model="llama4")

# 여러 문서 로드
loader = DirectoryLoader(
    "./docs/",
    glob="**/*.txt",
    loader_cls=TextLoader,
    loader_kwargs={"encoding": "utf-8"}
)
documents = loader.load()

def multi_doc_qa(question: str, documents: list) -> str:
    # 문서 내용 합치기 (출처 포함)
    context_parts = []
    for doc in documents:
        source = doc.metadata.get("source", "unknown")
        context_parts.append(f"[출처: {source}]\n{doc.page_content}")

    context = "\n\n---\n\n".join(context_parts)

    prompt = ChatPromptTemplate.from_template("""
다음 문서들을 참고하여 질문에 답변해주세요.
답변할 때 어느 문서에서 정보를 찾았는지 출처를 밝혀주세요.

문서들:
{context}

질문: {question}

답변:
""")

    chain = prompt | llm | StrOutputParser()
    return chain.invoke({"context": context, "question": question})


# 사용
answer = multi_doc_qa("회사의 주요 제품은 무엇인가요?", documents)
print(answer)
