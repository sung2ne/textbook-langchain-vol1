from langchain_ollama import ChatOllama

llm = ChatOllama(model="llama4")

# 첫 번째 대화
response1 = llm.invoke("내 이름은 철수야")
print(response1.content)  # 안녕하세요, 철수님!

# 두 번째 대화 - 이름을 기억하지 못함
response2 = llm.invoke("내 이름이 뭐야?")
print(response2.content)  # 죄송해요, 알려주신 적이 없어서 모르겠어요.
