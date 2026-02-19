from langchain_ollama import ChatOllama

# Ollama 모델 초기화
llm = ChatOllama(model="llama4")

# 질문하기
response = llm.invoke("안녕하세요!")

# 결과 출력
print(response.content)
