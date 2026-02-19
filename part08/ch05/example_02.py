def safe_invoke(chain, inputs: dict, default="처리 중 오류가 발생했습니다."):
    """안전한 체인 호출"""
    try:
        return chain.invoke(inputs)
    except Exception as e:
        print(f"[DEBUG] Error: {e}")
        return default
