from langchain_ollama import ChatOllama

# 일관된 응답 (temperature=0)
llm_consistent = ChatOllama(model="llama4", temperature=0)

# 창의적 응답 (temperature=1)
llm_creative = ChatOllama(model="llama4", temperature=1)

question = "AI의 미래를 한 문장으로 예측해줘"

print("Temperature 0:")
print(llm_consistent.invoke(question).content)

print("\nTemperature 1:")
print(llm_creative.invoke(question).content)
