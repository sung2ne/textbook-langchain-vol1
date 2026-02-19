from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough

llm = ChatOllama(model="llama4")
parser = StrOutputParser()

# 1단계: 개요 생성
outline_prompt = ChatPromptTemplate.from_template("""
'{topic}'에 대한 블로그 포스트 개요를 작성해주세요.

형식:
- 제목
- 서론 요점
- 본론 (3-4개 섹션)
- 결론 요점
""")

# 2단계: 본문 작성
content_prompt = ChatPromptTemplate.from_template("""
다음 개요를 바탕으로 블로그 포스트를 작성해주세요.

주제: {topic}
개요:
{outline}

요구사항:
- 친근한 말투
- 예시 포함
- 1000자 내외
""")

# 체인 구성
blog_chain = (
    RunnablePassthrough.assign(
        outline=outline_prompt | llm | parser
    )
    | content_prompt
    | llm
    | parser
)

# 사용
result = blog_chain.invoke({"topic": "Python 가상환경의 중요성"})
print(result)
