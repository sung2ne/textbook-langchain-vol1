from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate

llm = ChatOllama(model="llama4")

# 코드 설명 템플릿
template = PromptTemplate.from_template("""
다음 {language} 코드를 분석해주세요.

코드:
