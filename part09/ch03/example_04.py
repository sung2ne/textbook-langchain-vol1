# 방법 1: 환경 변수
import os
os.environ["LANGCHAIN_VERBOSE"] = "true"

# 방법 2: 전역 설정
from langchain.globals import set_debug
set_debug(True)

# 방법 3: 특정 체인만
chain = prompt | llm | parser
chain.with_config({"verbose": True})
