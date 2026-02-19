import tiktoken

# GPT-4o용 인코더
encoder = tiktoken.encoding_for_model("gpt-4o")

text = "안녕하세요, LangChain을 배우고 있습니다."
tokens = encoder.encode(text)

print(f"토큰 수: {len(tokens)}")
print(f"토큰 목록: {tokens}")
