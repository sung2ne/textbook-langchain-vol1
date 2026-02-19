from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

llm = ChatOllama(model="llama4")

def natural_to_sql(question: str, table_schema: str) -> str:
    prompt = ChatPromptTemplate.from_template("""
다음 테이블 스키마를 참고하여 자연어 질문을 SQL로 변환해주세요.

테이블 스키마:
{schema}

질문: {question}

SQL 쿼리만 출력해주세요 (설명 없이).
""")

    chain = prompt | llm | StrOutputParser()
    return chain.invoke({"schema": table_schema, "question": question})


# 사용
schema = """
테이블: products
컬럼:
- id (INT, PRIMARY KEY)
- name (VARCHAR)
- price (INT)
- category (VARCHAR)
- stock (INT)
"""

questions = [
    "모든 상품을 가격순으로 정렬해서 보여줘",
    "전자기기 카테고리의 평균 가격",
    "재고가 100개 미만인 상품들",
]

for q in questions:
    print(f"질문: {q}")
    print(f"SQL: {natural_to_sql(q, schema)}\n")
