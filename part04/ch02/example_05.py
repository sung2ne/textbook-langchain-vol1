from langchain_core.runnables import RunnableLambda

def add_exclamation(text):
    return text + "!"

chain = RunnableLambda(add_exclamation)
result = chain.invoke("Hello")
print(result)  # "Hello!"
