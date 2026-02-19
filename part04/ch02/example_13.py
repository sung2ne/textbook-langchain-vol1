from operator import itemgetter
from langchain_core.prompts import ChatPromptTemplate

prompt = ChatPromptTemplate.from_template("안녕하세요, {name}님!")

chain = (
    {"name": itemgetter("user_name")}  # user_name → name으로 매핑
    | prompt
)

messages = chain.invoke({"user_name": "철수", "email": "test@test.com"})
print(messages)
