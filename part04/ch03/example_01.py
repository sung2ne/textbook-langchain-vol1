from langchain_core.runnables import RunnableBranch, RunnableLambda

branch = RunnableBranch(
    # (조건 함수, 실행할 Runnable) 튜플의 리스트
    (lambda x: x > 10, RunnableLambda(lambda x: f"{x}는 10보다 큽니다")),
    (lambda x: x > 5, RunnableLambda(lambda x: f"{x}는 5보다 큽니다")),
    # 기본값 (조건이 모두 False일 때)
    RunnableLambda(lambda x: f"{x}는 5 이하입니다")
)

print(branch.invoke(15))  # 15는 10보다 큽니다
print(branch.invoke(7))   # 7는 5보다 큽니다
print(branch.invoke(3))   # 3는 5 이하입니다
