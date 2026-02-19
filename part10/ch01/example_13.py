def qa(question, documents):
    context = format_docs(documents)
    prompt = f"문서: {context}\n질문: {question}"
    return chain.invoke({"input": prompt})
