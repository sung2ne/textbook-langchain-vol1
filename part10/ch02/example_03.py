# 2권에서 배울 내용 미리보기
from langchain.chains import RetrievalQA

qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type="stuff",
    retriever=vectorstore.as_retriever()
)

answer = qa_chain.run("LangChain의 장점은?")
