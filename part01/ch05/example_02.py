import os

api_key = os.getenv("OPENAI_API_KEY")

if api_key:
    print(f"API 키가 설정되었습니다: {api_key[:10]}...")
else:
    print("API 키가 설정되지 않았습니다.")
