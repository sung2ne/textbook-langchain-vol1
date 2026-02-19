from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate

llm = ChatOllama(model="llama4")

# 코드 설명 템플릿
template = PromptTemplate.from_template("""
다음 {language} 코드를 분석해주세요.

코드:
{code}

다음 형식으로 답변해주세요:
1. 코드 설명
2. 주요 개념
3. 개선점 (있다면)
""")

# 템플릿 적용
prompt = template.format(
    language="Python",
    code="""
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)
"""
)

response = llm.invoke(prompt)
print(response.content)
