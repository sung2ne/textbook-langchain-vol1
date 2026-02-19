from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableBranch, RunnableLambda

llm = ChatOllama(model="llama4")

# 인사 체인
greeting_chain = RunnableLambda(
    lambda x: "안녕하세요! 무엇을 도와드릴까요? 코딩, 번역, 요약 등 다양한 작업을 도와드릴 수 있어요."
)

# 코딩 도우미
coding_prompt = ChatPromptTemplate.from_messages([
    ("system", "당신은 시니어 개발자입니다. 코드와 설명을 제공해주세요."),
    ("human", "{question}")
])
coding_chain = coding_prompt | llm | StrOutputParser()

# 번역 도우미
translate_prompt = ChatPromptTemplate.from_messages([
    ("system", "당신은 전문 번역가입니다."),
    ("human", "번역해주세요: {question}")
])
translate_chain = translate_prompt | llm | StrOutputParser()

# 요약 도우미
summary_prompt = ChatPromptTemplate.from_messages([
    ("system", "당신은 문서 요약 전문가입니다."),
    ("human", "요약해주세요: {question}")
])
summary_chain = summary_prompt | llm | StrOutputParser()

# 일반 대화
general_prompt = ChatPromptTemplate.from_messages([
    ("system", "당신은 친절한 어시스턴트입니다."),
    ("human", "{question}")
])
general_chain = general_prompt | llm | StrOutputParser()

# 분류 함수
def is_greeting(x):
    greetings = ["안녕", "하이", "hello", "hi", "반가워"]
    return any(g in x["question"].lower() for g in greetings)

def is_coding(x):
    keywords = ["코드", "함수", "버그", "에러", "구현", "python", "javascript"]
    return any(k in x["question"].lower() for k in keywords)

def is_translate(x):
    keywords = ["번역", "영어로", "한국어로", "translate"]
    return any(k in x["question"].lower() for k in keywords)

def is_summary(x):
    keywords = ["요약", "정리", "summarize"]
    return any(k in x["question"].lower() for k in keywords)

# 라우터
smart_assistant = RunnableBranch(
    (is_greeting, greeting_chain),
    (is_coding, coding_chain),
    (is_translate, translate_chain),
    (is_summary, summary_chain),
    general_chain
)

# 테스트
questions = [
    "안녕!",
    "Python으로 퀵소트 구현해줘",
    "I love programming을 한국어로 번역해줘",
    "이 긴 글을 요약해줘: ...",
    "오늘 뭐 먹을까?"
]

for q in questions:
    print(f"Q: {q}")
    print(f"A: {smart_assistant.invoke({'question': q})}\n")
