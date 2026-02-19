template = """
당신은 {role}입니다.

다음 질문에 답변해주세요.
질문: {question}

{format_instructions}
"""

# 사용
prompt = template.format(
    role="Python 전문가",
    question="리스트 컴프리헨션이 뭐야?",
    format_instructions="예시 코드를 포함해주세요."
)
