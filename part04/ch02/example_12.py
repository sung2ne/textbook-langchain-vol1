from operator import itemgetter

chain = itemgetter("name") | RunnableLambda(lambda x: f"Hello, {x}!")
result = chain.invoke({"name": "Alice", "age": 30})
print(result)  # "Hello, Alice!"
