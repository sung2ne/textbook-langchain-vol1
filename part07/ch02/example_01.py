from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.document_loaders import TextLoader

llm = ChatOllama(model="llama4")

# 문서 로드
loader = TextLoader("company_info.txt", encoding="utf-8")
documents = loader.load()
document_text = documents[0].page_content

# QA 프롬프트
prompt = ChatPromptTemplate.from_template("""
다음 문서를 참고하여 질문에 답변해주세요.
문서에 없는 내용은 "문서에서 해당 정보를 찾을 수 없습니다"라고 답변하세요.

문서:
{document}

질문: {question}

답변:
""")

chain = prompt | llm | StrOutputParser()

# 질문
response = chain.invoke({
    "document": document_text,
    "question": "회사 설립일은 언제인가요?"
})
print(response)
