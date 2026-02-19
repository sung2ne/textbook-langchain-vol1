import time
from functools import wraps
from collections import defaultdict


class PerformanceMonitor:
    def __init__(self):
        self.metrics = defaultdict(list)

    def measure(self, name: str):
        """데코레이터로 시간 측정"""
        def decorator(func):
            @wraps(func)
            def wrapper(*args, **kwargs):
                start = time.time()
                result = func(*args, **kwargs)
                elapsed = time.time() - start

                self.metrics[name].append(elapsed)
                return result
            return wrapper
        return decorator

    def get_stats(self, name: str) -> dict:
        """통계 조회"""
        times = self.metrics.get(name, [])
        if not times:
            return {}

        return {
            "count": len(times),
            "avg": sum(times) / len(times),
            "min": min(times),
            "max": max(times),
            "total": sum(times)
        }

    def report(self) -> str:
        """전체 리포트"""
        lines = ["=== 성능 리포트 ==="]
        for name in self.metrics:
            stats = self.get_stats(name)
            lines.append(f"\n{name}:")
            lines.append(f"  호출 횟수: {stats['count']}")
            lines.append(f"  평균 시간: {stats['avg']:.3f}초")
            lines.append(f"  최소/최대: {stats['min']:.3f}초 / {stats['max']:.3f}초")
        return "\n".join(lines)


# 사용
monitor = PerformanceMonitor()


class ProductAnalyzer:
    @monitor.measure("analyze")
    def analyze(self, product):
        # 분석 로직
        pass

    @monitor.measure("compare")
    def compare(self, products):
        # 비교 로직
        pass


# 리포트 출력
print(monitor.report())
