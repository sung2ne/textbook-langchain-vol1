from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

prompt = ChatPromptTemplate.from_messages([
    ("system", "{source_lang}를 {target_lang}로 번역하는 전문 번역가입니다."),
    ("human", "번역해주세요: {text}")
])

llm = ChatOllama(model="llama4")
parser = StrOutputParser()

translate_chain = prompt | llm | parser

# 사용
result = translate_chain.invoke({
    "source_lang": "한국어",
    "target_lang": "영어",
    "text": "안녕하세요, 반갑습니다."
})

print(result)  # Hello, nice to meet you.
