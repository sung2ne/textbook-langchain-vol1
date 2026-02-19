# 검색 결과를 LLM이 재평가
results = vectorstore.similarity_search(query, k=10)
reranked = rerank_with_llm(query, results)
