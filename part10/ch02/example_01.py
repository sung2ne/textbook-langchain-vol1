# 2권에서 배울 내용 미리보기
from langchain_ollama import OllamaEmbeddings

embeddings = OllamaEmbeddings(model="nomic-embed-text")

# 텍스트 → 벡터
vector = embeddings.embed_query("LangChain이 뭐야?")
print(len(vector))  # 768차원 벡터
