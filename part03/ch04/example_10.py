from langchain_core.output_parsers import JsonOutputParser

parser = JsonOutputParser()

try:
    result = parser.invoke("이것은 JSON이 아닙니다")
except Exception as e:
    print(f"파싱 실패: {e}")
    # 대체 로직 실행
