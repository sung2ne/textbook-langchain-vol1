from langchain_core.runnables import RunnablePassthrough

chain = RunnablePassthrough.assign(
    uppercase=lambda x: x["text"].upper()
)

result = chain.invoke({"text": "hello"})
print(result)  # {"text": "hello", "uppercase": "HELLO"}
