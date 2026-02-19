# 1. invoke 호출
chain.invoke({"question": "Python이 뭐야?"})

# 2. prompt 단계
#    입력: {"question": "Python이 뭐야?"}
#    출력: [SystemMessage(...), HumanMessage(content="Python이 뭐야?")]

# 3. llm 단계
#    입력: [SystemMessage(...), HumanMessage(...)]
#    출력: AIMessage(content="Python은 1991년에...")

# 4. parser 단계
#    입력: AIMessage(content="Python은 1991년에...")
#    출력: "Python은 1991년에..."
