from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import json

llm = ChatOllama(model="llama4")

def transform_data(data: str, instruction: str) -> str:
    prompt = ChatPromptTemplate.from_template("""
다음 데이터를 요청에 맞게 변환해주세요.

원본 데이터:
{data}

요청: {instruction}

변환된 데이터만 출력해주세요 (설명 없이).
""")

    chain = prompt | llm | StrOutputParser()
    return chain.invoke({"data": data, "instruction": instruction})


# 사용
csv_data = """name,price
노트북,1200000
키보드,80000"""

# CSV → JSON 변환
json_result = transform_data(csv_data, "CSV를 JSON 배열로 변환해줘")
print(json_result)

# 단위 변환
result = transform_data(csv_data, "가격을 만원 단위로 바꿔줘 (예: 1200000 → 120만원)")
print(result)
