from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough

llm = ChatOllama(model="llama4")

# 1단계: 요약 생성
summary_prompt = ChatPromptTemplate.from_template(
    "다음 텍스트를 한 문장으로 요약해주세요: {text}"
)

# 2단계: 요약에 대한 질문 답변
qa_prompt = ChatPromptTemplate.from_template(
    """원본: {text}
    요약: {summary}

    질문: {question}"""
)

# 체인 구성
chain = (
    RunnablePassthrough.assign(
        summary=summary_prompt | llm | StrOutputParser()
    )
    | qa_prompt
    | llm
    | StrOutputParser()
)

result = chain.invoke({
    "text": "Python은 1991년 귀도 반 로섬이 만든 프로그래밍 언어입니다. 읽기 쉬운 문법이 특징입니다.",
    "question": "누가 만들었나요?"
})
print(result)
