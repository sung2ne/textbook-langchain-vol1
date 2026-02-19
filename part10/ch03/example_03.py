# 각 단계 출력
result1 = prompt.invoke({"question": "테스트"})
print("프롬프트 결과:", result1)

result2 = llm.invoke(result1)
print("LLM 결과:", result2)

result3 = parser.invoke(result2)
print("파싱 결과:", result3)
