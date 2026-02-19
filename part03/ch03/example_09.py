translate_template = ChatPromptTemplate.from_messages([
    ("system", "당신은 전문 번역가입니다. {source_lang}를 {target_lang}로 번역합니다."),
    ("human", "다음 텍스트를 번역해주세요:\n\n{text}")
])

chain = translate_template | llm
response = chain.invoke({
    "source_lang": "영어",
    "target_lang": "한국어",
    "text": "Hello, how are you?"
})
