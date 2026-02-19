# LCEL
chain = prompt | llm | parser
result = chain.invoke(inputs)

# 없이
messages = prompt.format_messages(**inputs)
response = llm.invoke(messages)
result = parser.invoke(response)
