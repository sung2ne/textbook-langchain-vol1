import traceback
from datetime import datetime


class ErrorTracker:
    def __init__(self, error_file: str = "errors.log"):
        self.error_file = error_file

    def track(self, error: Exception, context: dict = None):
        """에러 기록"""
        entry = [
            f"=== Error at {datetime.now().isoformat()} ===",
            f"Type: {type(error).__name__}",
            f"Message: {str(error)}",
            f"Context: {context}",
            "Traceback:",
            traceback.format_exc(),
            ""
        ]

        with open(self.error_file, "a", encoding="utf-8") as f:
            f.write("\n".join(entry))


error_tracker = ErrorTracker()


def safe_process(func):
    """에러 처리 데코레이터"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            error_tracker.track(e, {
                "function": func.__name__,
                "args": str(args)[:100],
            })
            raise
    return wrapper
