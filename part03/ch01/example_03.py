from langchain_ollama import ChatOllama

llm = ChatOllama(model="llama4")

questions = [
    "Python이 뭐야?",
    "1 + 1은?",
    "오늘 기분이 어때?"
]

for question in questions:
    response = llm.invoke(question)
    print(f"Q: {question}")
    print(f"A: {response.content}\n")
