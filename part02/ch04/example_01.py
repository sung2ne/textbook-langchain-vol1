# Ollama 사용
from langchain_ollama import ChatOllama
llm = ChatOllama(model="llama4")

# OpenAI로 변경
from langchain_openai import ChatOpenAI
llm = ChatOpenAI(model="gpt-4o-mini")
