results = chain.batch([
    {"question": "Python이 뭐야?"},
    {"question": "JavaScript가 뭐야?"},
    {"question": "Rust가 뭐야?"}
])

for r in results:
    print(r[:50], "...")
