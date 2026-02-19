# 벡터 검색
def search(query):
    return vectorstore.similarity_search(query, k=5)
