from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

llm = ChatOllama(model="llama4")

relevance_prompt = ChatPromptTemplate.from_template("""
질문: {question}

다음 텍스트가 질문과 관련이 있나요?
텍스트: {chunk}

"yes" 또는 "no"로만 답변해주세요.
""")

def filter_relevant_chunks(question: str, chunks: list) -> list:
    chain = relevance_prompt | llm | StrOutputParser()
    relevant = []

    for chunk in chunks:
        result = chain.invoke({"question": question, "chunk": chunk})
        if "yes" in result.lower():
            relevant.append(chunk)

    return relevant


# 사용
chunks = ["청크1...", "청크2...", "청크3..."]
question = "LangChain의 주요 기능은?"
relevant_chunks = filter_relevant_chunks(question, chunks)
