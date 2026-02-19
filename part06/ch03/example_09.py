from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import JsonOutputParser

llm = ChatOllama(model="llama4")
parser = JsonOutputParser()

extract_prompt = ChatPromptTemplate.from_template("""
다음 텍스트에서 정보를 추출해주세요.

텍스트:
{text}

다음 JSON 형식으로 응답해주세요:
{{"people": ["이름1", "이름2"], "places": ["장소1", "장소2"], "dates": ["날짜1"]}}
""")

chain = extract_prompt | llm | parser

text = """
2024년 1월 15일, 서울에서 김철수와 이영희가 만났습니다.
그들은 부산으로 여행을 계획하고 있습니다.
"""

result = chain.invoke({"text": text})
print(result)
# {"people": ["김철수", "이영희"], "places": ["서울", "부산"], "dates": ["2024년 1월 15일"]}
