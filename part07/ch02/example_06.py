def is_relevant_question(question: str, document: str) -> bool:
    """질문이 문서와 관련 있는지 확인"""
    prompt = ChatPromptTemplate.from_template("""
다음 질문이 문서의 내용과 관련이 있는지 판단해주세요.

문서 요약:
{document_summary}

질문: {question}

"yes" 또는 "no"로만 답변해주세요.
""")

    chain = prompt | llm | StrOutputParser()

    # 문서 요약 (처음 500자만 사용)
    summary = document[:500] + "..." if len(document) > 500 else document

    result = chain.invoke({
        "document_summary": summary,
        "question": question
    })

    return "yes" in result.lower()


# 사용
document = "ABC 회사는 AI 서비스를 제공합니다..."

print(is_relevant_question("회사 서비스가 뭐야?", document))  # True
print(is_relevant_question("오늘 날씨가 어때?", document))   # False
