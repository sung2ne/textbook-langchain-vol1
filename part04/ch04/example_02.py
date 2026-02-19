from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

llm = ChatOllama(model="llama4")
parser = StrOutputParser()

# 분석 체인
analysis_prompt = ChatPromptTemplate.from_template("""
다음 {language} 코드를 분석해주세요.
