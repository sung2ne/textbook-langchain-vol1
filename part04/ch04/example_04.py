from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

llm = ChatOllama(model="llama4")
parser = StrOutputParser()

# 요약 체인
summary_prompt = ChatPromptTemplate.from_template("""
다음 문서를 3문장으로 요약해주세요.

문서:
{document}

요약:""")

# 키워드 추출 체인
keyword_prompt = ChatPromptTemplate.from_template("""
다음 문서의 핵심 키워드 5개를 추출해주세요.

문서:
{document}

키워드 (쉼표로 구분):""")

# 감정 분석 체인
sentiment_prompt = ChatPromptTemplate.from_template("""
다음 문서의 전체적인 톤을 분석해주세요.

문서:
{document}

톤 (긍정적/부정적/중립적):""")

# 병렬 실행
analysis_chain = {
    "summary": summary_prompt | llm | parser,
    "keywords": keyword_prompt | llm | parser,
    "sentiment": sentiment_prompt | llm | parser,
}

# 사용
document = """
최근 인공지능 기술의 발전은 놀라운 수준입니다.
특히 대규모 언어 모델(LLM)의 등장으로 자연어 처리 분야에서
혁명적인 변화가 일어나고 있습니다. ChatGPT, Claude, Llama 등
다양한 모델들이 등장하면서 일반인도 쉽게 AI를 활용할 수 있게 되었습니다.
하지만 이러한 기술 발전에는 윤리적 고려사항도 따릅니다.
"""

result = analysis_chain.invoke({"document": document})
print(f"요약: {result['summary']}")
print(f"키워드: {result['keywords']}")
print(f"톤: {result['sentiment']}")
