# 저장 (JSON)
template.save("my_template.json")

# 불러오기
from langchain_core.prompts import load_prompt
loaded_template = load_prompt("my_template.json")
