from langchain_core.runnables import RunnableLambda

# 여러 모델 병렬 실행
multi_model = {
    "model_a": chain_a,
    "model_b": chain_b,
}

# 결과 선택
def select_best(results):
    # 더 긴 응답 선택 (예시)
    if len(results["model_a"]) > len(results["model_b"]):
        return results["model_a"]
    return results["model_b"]

final_chain = multi_model | RunnableLambda(select_best)
