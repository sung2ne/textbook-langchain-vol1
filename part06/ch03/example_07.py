from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_text_splitters import RecursiveCharacterTextSplitter

llm = ChatOllama(model="llama4")
parser = StrOutputParser()

# 청크별 요약 프롬프트
map_prompt = ChatPromptTemplate.from_template(
    "다음 텍스트의 핵심 내용을 2문장으로 요약해주세요:\n\n{text}"
)

# 최종 요약 프롬프트
reduce_prompt = ChatPromptTemplate.from_template(
    "다음 요약들을 종합하여 최종 요약을 작성해주세요:\n\n{summaries}"
)

def map_reduce_summarize(text: str, chunk_size: int = 1000) -> str:
    # 1. 텍스트 분할
    splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=100)
    chunks = splitter.split_text(text)

    # 2. Map: 각 청크 요약
    map_chain = map_prompt | llm | parser
    summaries = []
    for chunk in chunks:
        summary = map_chain.invoke({"text": chunk})
        summaries.append(summary)

    # 3. Reduce: 요약들 통합
    reduce_chain = reduce_prompt | llm | parser
    final_summary = reduce_chain.invoke({
        "summaries": "\n\n".join(summaries)
    })

    return final_summary


# 사용
long_document = "..." # 긴 문서
summary = map_reduce_summarize(long_document)
print(summary)
