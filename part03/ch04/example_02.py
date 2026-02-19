from langchain_ollama import ChatOllama
from langchain_core.output_parsers import StrOutputParser

llm = ChatOllama(model="llama4")
parser = StrOutputParser()

response = llm.invoke("안녕하세요!")
print(type(response))  # <class 'AIMessage'>

parsed = parser.invoke(response)
print(type(parsed))    # <class 'str'>
print(parsed)          # 안녕하세요! 무엇을 도와드릴까요?
