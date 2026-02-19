import json
from datetime import datetime
from pathlib import Path


class RequestLogger:
    def __init__(self, log_dir: str = "logs"):
        self.log_dir = Path(log_dir)
        self.log_dir.mkdir(exist_ok=True)

    def log_request(self, session_id: str, user_input: str, response: str):
        """요청/응답 기록"""
        timestamp = datetime.now().isoformat()

        entry = {
            "timestamp": timestamp,
            "session_id": session_id,
            "input": user_input,
            "response": response,
            "input_length": len(user_input),
            "response_length": len(response)
        }

        # 일별 로그 파일
        date_str = datetime.now().strftime("%Y-%m-%d")
        log_file = self.log_dir / f"requests_{date_str}.jsonl"

        with open(log_file, "a", encoding="utf-8") as f:
            f.write(json.dumps(entry, ensure_ascii=False) + "\n")


# 사용
request_logger = RequestLogger()


class ProductChatbot:
    def process(self, user_input: str, session_id: str = "default") -> str:
        response = self._process_internal(user_input, session_id)

        # 로깅
        request_logger.log_request(session_id, user_input, response)

        return response
