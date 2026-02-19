from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate

llm = ChatOllama(model="llama4")

prompt = ChatPromptTemplate.from_template("""
다음 문서를 3문장으로 요약해주세요.

{document}

요약:
""")

chain = prompt | llm

response = chain.invoke({"document": document_text})
