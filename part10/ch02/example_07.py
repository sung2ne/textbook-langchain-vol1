# 키워드 검색
def search(query):
    keywords = query.split()
    return [p for p in products if any(k in p.name for k in keywords)]
