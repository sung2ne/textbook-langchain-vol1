import time


def benchmark(func, *args, iterations=10):
    """벤치마크 실행"""
    times = []
    for _ in range(iterations):
        start = time.time()
        func(*args)
        times.append(time.time() - start)

    return {
        "avg": sum(times) / len(times),
        "min": min(times),
        "max": max(times)
    }


# 사용
result = benchmark(chatbot.chat, "가장 좋은 상품 추천해줘", iterations=5)
print(f"평균: {result['avg']:.2f}초")
