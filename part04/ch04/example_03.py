from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough, RunnableLambda

llm = ChatOllama(model="llama4")
parser = StrOutputParser()

# 언어 감지
detect_prompt = ChatPromptTemplate.from_template("""
다음 텍스트의 언어를 감지해주세요.
텍스트: {question}
언어 코드만 답변 (ko/en/ja/zh):""")

# 답변 생성
answer_prompt = ChatPromptTemplate.from_template("""
다음 질문에 답변해주세요.

질문: {question}

{language_instruction}
""")

def get_language_instruction(inputs):
    lang = inputs["language"].strip().lower()
    instructions = {
        "ko": "한국어로 답변해주세요.",
        "en": "Please answer in English.",
        "ja": "日本語で答えてください。",
        "zh": "请用中文回答。",
    }
    return {
        **inputs,
        "language_instruction": instructions.get(lang, instructions["en"])
    }

# 체인 구성
faq_chain = (
    RunnablePassthrough.assign(
        language=detect_prompt | llm | parser
    )
    | RunnableLambda(get_language_instruction)
    | answer_prompt
    | llm
    | parser
)

# 테스트
questions = [
    "Python이 뭐야?",
    "What is Python?",
    "Pythonとは何ですか？",
]

for q in questions:
    print(f"Q: {q}")
    print(f"A: {faq_chain.invoke({'question': q})}\n")
