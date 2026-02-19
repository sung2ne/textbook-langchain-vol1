from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

prompt = ChatPromptTemplate.from_messages([
    ("system", "당신은 {role}입니다."),
    MessagesPlaceholder(variable_name="chat_history"),
    ("human", "{question}")
])

# format 할 때
messages = prompt.format_messages(
    role="Python 튜터",
    chat_history=[
        HumanMessage(content="안녕"),
        AIMessage(content="안녕하세요!")
    ],
    question="for 루프가 뭐야?"
)
