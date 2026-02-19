from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableLambda, RunnablePassthrough

llm = ChatOllama(model="llama4")

# 1단계: 질문 분류
classifier_prompt = ChatPromptTemplate.from_template("""
다음 질문의 유형을 분류해주세요.

질문: {question}

유형 (code/math/general 중 하나만 답변):""")

classifier_chain = classifier_prompt | llm | StrOutputParser()

# 2단계: 유형별 체인 (위와 동일)
code_chain = ChatPromptTemplate.from_messages([
    ("system", "당신은 프로그래밍 전문가입니다."),
    ("human", "{question}")
]) | llm | StrOutputParser()

math_chain = ChatPromptTemplate.from_messages([
    ("system", "당신은 수학 선생님입니다."),
    ("human", "{question}")
]) | llm | StrOutputParser()

general_chain = ChatPromptTemplate.from_messages([
    ("system", "당신은 친절한 어시스턴트입니다."),
    ("human", "{question}")
]) | llm | StrOutputParser()

# 라우터 함수
def route_by_type(inputs):
    question_type = inputs["type"].strip().lower()
    question = inputs["question"]

    if "code" in question_type:
        return code_chain.invoke({"question": question})
    elif "math" in question_type:
        return math_chain.invoke({"question": question})
    else:
        return general_chain.invoke({"question": question})

# 전체 체인
full_chain = (
    RunnablePassthrough.assign(
        type=classifier_chain
    )
    | RunnableLambda(route_by_type)
)

result = full_chain.invoke({"question": "피보나치 수열 구현해줘"})
print(result)
