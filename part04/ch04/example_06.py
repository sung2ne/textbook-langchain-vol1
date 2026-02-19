from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough, RunnableLambda

llm = ChatOllama(model="llama4")
parser = StrOutputParser()

# 체인 1: 아이디어 생성
idea_prompt = ChatPromptTemplate.from_template(
    "{topic}에 대한 창의적인 아이디어 3가지를 제안해주세요."
)
idea_chain = idea_prompt | llm | parser

# 체인 2: 아이디어 평가
evaluate_prompt = ChatPromptTemplate.from_template("""
다음 아이디어들을 실현 가능성 관점에서 평가해주세요.

아이디어:
{ideas}

각 아이디어에 대해 점수(1-10)와 이유를 적어주세요.
""")
evaluate_chain = evaluate_prompt | llm | parser

# 체인 3: 최종 추천
recommend_prompt = ChatPromptTemplate.from_template("""
다음 평가를 바탕으로 가장 좋은 아이디어를 추천하고 실행 계획을 제안해주세요.

평가:
{evaluation}
""")
recommend_chain = recommend_prompt | llm | parser

# 전체 파이프라인
full_pipeline = (
    RunnablePassthrough.assign(ideas=idea_chain)
    | RunnablePassthrough.assign(evaluation=evaluate_chain)
    | recommend_chain
)

# 사용
result = full_pipeline.invoke({"topic": "사이드 프로젝트"})
print(result)
