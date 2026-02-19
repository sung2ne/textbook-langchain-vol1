from langchain_core.runnables import RunnableLambda

@RunnableLambda
def process_text(text):
    return text.upper().strip()

result = process_text.invoke("  hello  ")
print(result)  # "HELLO"
