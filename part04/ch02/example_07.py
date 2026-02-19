from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableLambda

llm = ChatOllama(model="llama4")

# 전처리: 입력 정리
def preprocess(inputs):
    return {"question": inputs["question"].strip().lower()}

# 후처리: 결과 포맷팅
def postprocess(response):
    return f"🤖 AI: {response}"

prompt = ChatPromptTemplate.from_template("{question}에 대해 간단히 설명해줘.")

chain = (
    RunnableLambda(preprocess)
    | prompt
    | llm
    | StrOutputParser()
    | RunnableLambda(postprocess)
)

result = chain.invoke({"question": "  PYTHON  "})
print(result)  # 🤖 AI: Python은...
