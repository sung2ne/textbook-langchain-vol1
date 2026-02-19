from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough

llm = ChatOllama(model="llama4")

# 질문을 영어로 번역하는 체인
translate_prompt = ChatPromptTemplate.from_template(
    "다음 한국어를 영어로 번역해주세요: {question}"
)

chain = (
    {"question": RunnablePassthrough()}
    | translate_prompt
    | llm
    | StrOutputParser()
)

result = chain.invoke("안녕하세요")
print(result)  # Hello
