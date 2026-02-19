# 토큰: LLM이 처리하는 텍스트 단위
# 한국어는 영어보다 더 많은 토큰 사용

import tiktoken
enc = tiktoken.get_encoding("cl100k_base")
print(len(enc.encode("안녕하세요")))  # 약 5개 토큰
