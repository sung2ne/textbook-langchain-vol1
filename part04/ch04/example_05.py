from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

llm = ChatOllama(model="llama4")
parser = StrOutputParser()

prompt = ChatPromptTemplate.from_messages([
    ("system", "당신은 친절한 AI 어시스턴트입니다."),
    ("human", "{question}")
])

chat_chain = prompt | llm | parser

def chat(question):
    print("AI: ", end="", flush=True)
    for chunk in chat_chain.stream({"question": question}):
        print(chunk, end="", flush=True)
    print()  # 줄바꿈

# 대화형 루프
while True:
    user_input = input("You: ")
    if user_input.lower() in ["quit", "exit", "q"]:
        break
    chat(user_input)
