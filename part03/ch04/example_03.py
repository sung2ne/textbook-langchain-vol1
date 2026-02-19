from langchain_ollama import ChatOllama
from langchain_core.output_parsers import StrOutputParser

llm = ChatOllama(model="llama4")
parser = StrOutputParser()

chain = llm | parser

result = chain.invoke("안녕하세요!")
print(type(result))  # <class 'str'>
print(result)        # 안녕하세요! 무엇을 도와드릴까요?
