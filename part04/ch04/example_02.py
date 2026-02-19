from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

llm = ChatOllama(model="llama4")
parser = StrOutputParser()

# 분석 체인
analysis_prompt = ChatPromptTemplate.from_template("""
다음 {language} 코드를 분석해주세요.

{code}

다음 항목을 평가해주세요:
1. 가독성 (1-10점)
2. 효율성 (1-10점)
3. 잠재적 버그
4. 개선 제안
""")

# 개선 코드 생성 체인
improve_prompt = ChatPromptTemplate.from_template("""
다음 분석을 바탕으로 개선된 코드를 작성해주세요.

원본 코드:
{code}

분석 결과:
{analysis}

개선된 코드만 출력해주세요.
""")

# 전체 체인
review_chain = (
    RunnablePassthrough.assign(
        analysis=analysis_prompt | llm | parser
    )
    | improve_prompt
    | llm
    | parser
)

# 사용
code = """
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)
"""

result = review_chain.invoke({
    "language": "python",
    "code": code
})
print(result)
