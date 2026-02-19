from langchain_ollama import ChatOllama
from langchain_community.document_loaders import WebBaseLoader
from langchain_core.prompts import ChatPromptTemplate

llm = ChatOllama(model="llama4")

# 웹 페이지 로드
loader = WebBaseLoader("https://news.ycombinator.com/")
docs = loader.load()

# 프롬프트 구성
prompt = ChatPromptTemplate.from_template("""
다음은 Hacker News의 내용입니다.

{content}

위 내용에서 가장 흥미로운 기사 3개를 선택하고, 각각 한 문장으로 요약해주세요.
""")

# 체인 실행
chain = prompt | llm
response = chain.invoke({"content": docs[0].page_content[:3000]})
print(response.content)
