def get_llm_for_task(task: str):
    """작업별 최적 모델 선택"""
    if task == "simple_qa":
        # 간단한 질문은 작은 모델
        return ChatOllama(model="llama4", num_ctx=2048)
    elif task == "analysis":
        # 분석은 큰 컨텍스트
        return ChatOllama(model="llama4", num_ctx=8192)
    elif task == "comparison":
        # 비교는 기본 설정
        return ChatOllama(model="llama4")
    else:
        return ChatOllama(model="llama4")
