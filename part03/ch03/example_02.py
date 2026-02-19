from langchain_core.prompts import PromptTemplate

# 템플릿 생성
template = PromptTemplate.from_template(
    "{topic}에 대해 {style}로 설명해줘"
)

# 템플릿 사용
prompt = template.format(topic="Python", style="초보자도 이해할 수 있게")
print(prompt)
