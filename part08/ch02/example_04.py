from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from models import Product
from typing import Optional

llm = ChatOllama(model="llama4")


def extract_with_llm(html: str, url: str = "") -> Optional[Product]:
    """LLM을 사용하여 HTML에서 상품 정보 추출"""

    # HTML에서 텍스트만 추출
    soup = BeautifulSoup(html, "html.parser")

    # 스크립트, 스타일 제거
    for tag in soup(["script", "style", "nav", "footer"]):
        tag.decompose()

    text = soup.get_text(separator="\n", strip=True)

    # 텍스트가 너무 길면 자르기
    text = text[:3000]

    prompt = ChatPromptTemplate.from_template("""
다음 웹 페이지 텍스트에서 상품 정보를 추출해주세요.

웹 페이지 내용:
{text}

다음 JSON 형식으로 응답해주세요:
{{
    "name": "상품명",
    "price": 가격(숫자만),
    "description": "상품 설명 (100자 이내)",
    "specs": {{
        "항목1": "값1",
        "항목2": "값2"
    }}
}}

상품 정보를 찾을 수 없으면 null을 반환하세요.
JSON만 출력하세요.
""")

    chain = prompt | llm | JsonOutputParser()

    try:
        result = chain.invoke({"text": text})

        if result and result.get("name"):
            return Product(
                name=result["name"],
                price=result.get("price", 0),
                url=url,
                description=result.get("description", ""),
                specs=result.get("specs", {})
            )
    except Exception as e:
        print(f"LLM 추출 실패: {e}")

    return None


# 사용
product = extract_with_llm(TEST_HTML_1, "https://example.com/product")
if product:
    print(product.to_text())
