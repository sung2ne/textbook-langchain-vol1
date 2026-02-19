from langchain_core.runnables import RunnableParallel

parallel = RunnableParallel(
    upper=RunnableLambda(lambda x: x.upper()),
    lower=RunnableLambda(lambda x: x.lower()),
    length=RunnableLambda(lambda x: len(x))
)

result = parallel.invoke("Hello")
print(result)  # {"upper": "HELLO", "lower": "hello", "length": 5}
