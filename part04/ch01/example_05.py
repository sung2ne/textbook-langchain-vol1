for chunk in chain.stream({"question": "Python에 대해 설명해줘"}):
    print(chunk, end="", flush=True)
