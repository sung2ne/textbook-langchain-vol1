from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate

llm = ChatOllama(model="llama4")

prompt = ChatPromptTemplate.from_template("{question}")
chain = prompt | llm


def stream_response(question: str):
    """스트리밍 응답"""
    print("AI: ", end="", flush=True)

    for chunk in chain.stream({"question": question}):
        # 청크 내용 출력
        content = chunk.content if hasattr(chunk, 'content') else str(chunk)
        print(content, end="", flush=True)

    print()  # 줄바꿈


# 사용
stream_response("LangChain이 뭐야?")
