# 키워드 검색 결과와 벡터 검색 결과를 합침
keyword_results = keyword_search(query)
vector_results = vector_search(query)
final_results = merge_results(keyword_results, vector_results)
