import json
from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

llm = ChatOllama(model="llama4")

# JSON 로드
with open("users.json", "r", encoding="utf-8") as f:
    data = json.load(f)

def query_json(data: dict, question: str) -> str:
    # JSON을 보기 좋게 변환
    data_text = json.dumps(data, ensure_ascii=False, indent=2)

    prompt = ChatPromptTemplate.from_template("""
다음 JSON 데이터를 분석해주세요.

{data}

질문: {question}
""")

    chain = prompt | llm | StrOutputParser()
    return chain.invoke({"data": data_text, "question": question})


# 예시 JSON
example_data = {
    "users": [
        {"name": "김철수", "age": 28, "city": "서울"},
        {"name": "이영희", "age": 32, "city": "부산"},
        {"name": "박민수", "age": 25, "city": "서울"},
    ]
}

print(query_json(example_data, "서울에 사는 사용자는 몇 명이야?"))
print(query_json(example_data, "평균 나이는?"))
