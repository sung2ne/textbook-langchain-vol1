refine_prompt = ChatPromptTemplate.from_template("""
기존 요약:
{existing_summary}

추가 내용:
{new_content}

위 내용을 반영하여 요약을 업데이트해주세요.
""")

def refine_summarize(chunks: list) -> str:
    summary = ""

    for i, chunk in enumerate(chunks):
        if i == 0:
            # 첫 청크: 초기 요약
            initial_chain = map_prompt | llm | parser
            summary = initial_chain.invoke({"text": chunk})
        else:
            # 이후 청크: 요약 개선
            refine_chain = refine_prompt | llm | parser
            summary = refine_chain.invoke({
                "existing_summary": summary,
                "new_content": chunk
            })

    return summary
