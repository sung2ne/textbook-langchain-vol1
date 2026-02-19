from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableBranch, RunnableLambda

llm = ChatOllama(model="llama4")

# 코드 질문용 체인
code_prompt = ChatPromptTemplate.from_messages([
    ("system", "당신은 프로그래밍 전문가입니다. 코드 예시와 함께 설명해주세요."),
    ("human", "{question}")
])
code_chain = code_prompt | llm | StrOutputParser()

# 일반 질문용 체인
general_prompt = ChatPromptTemplate.from_messages([
    ("system", "당신은 친절한 어시스턴트입니다."),
    ("human", "{question}")
])
general_chain = general_prompt | llm | StrOutputParser()

# 수학 질문용 체인
math_prompt = ChatPromptTemplate.from_messages([
    ("system", "당신은 수학 선생님입니다. 단계별로 풀이해주세요."),
    ("human", "{question}")
])
math_chain = math_prompt | llm | StrOutputParser()

# 질문 분류 함수
def is_code_question(inputs):
    keywords = ["코드", "함수", "클래스", "python", "javascript", "프로그래밍"]
    question = inputs["question"].lower()
    return any(kw in question for kw in keywords)

def is_math_question(inputs):
    keywords = ["계산", "수학", "더하기", "빼기", "곱하기", "방정식", "+", "-", "*", "/"]
    question = inputs["question"].lower()
    return any(kw in question for kw in keywords)

# 분기 체인
router = RunnableBranch(
    (is_code_question, code_chain),
    (is_math_question, math_chain),
    general_chain  # 기본
)

# 테스트
print(router.invoke({"question": "Python에서 리스트 정렬하는 코드 알려줘"}))
print("---")
print(router.invoke({"question": "2 + 3 * 4는 얼마야?"}))
print("---")
print(router.invoke({"question": "오늘 날씨 어때?"}))
