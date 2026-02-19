from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import pandas as pd

llm = ChatOllama(model="llama4")

df = pd.read_csv("products.csv")

def ask_about_data(df: pd.DataFrame, question: str) -> str:
    # DataFrame을 텍스트로 변환
    data_text = df.to_string(index=False)

    prompt = ChatPromptTemplate.from_template("""
다음은 상품 데이터입니다.

{data}

질문: {question}

위 데이터를 분석하여 답변해주세요.
""")

    chain = prompt | llm | StrOutputParser()
    return chain.invoke({"data": data_text, "question": question})


# 사용
print(ask_about_data(df, "가장 비싼 상품은?"))
print(ask_about_data(df, "전자기기 카테고리의 평균 가격은?"))
print(ask_about_data(df, "재고가 100개 이상인 상품은?"))
