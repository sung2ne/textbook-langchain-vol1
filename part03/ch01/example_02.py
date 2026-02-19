from langchain_ollama import ChatOllama

llm = ChatOllama(model="llama4")
response = llm.invoke("안녕하세요!")

print(type(response))
print(response)
