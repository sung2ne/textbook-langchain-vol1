# LCEL 없이 작성하면
formatted_prompt = prompt.format_messages(...)
response = llm.invoke(formatted_prompt)
result = parser.invoke(response)
