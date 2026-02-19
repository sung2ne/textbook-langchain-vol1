import hashlib
import json
from pathlib import Path
from datetime import datetime, timedelta


class ResponseCache:
    def __init__(self, cache_dir: str = ".cache", ttl_hours: int = 24):
        self.cache_dir = Path(cache_dir)
        self.cache_dir.mkdir(exist_ok=True)
        self.ttl = timedelta(hours=ttl_hours)

    def _get_key(self, question: str, context: str = "") -> str:
        """캐시 키 생성"""
        data = f"{question}:{context}"
        return hashlib.md5(data.encode()).hexdigest()

    def get(self, question: str, context: str = "") -> str | None:
        """캐시에서 조회"""
        key = self._get_key(question, context)
        cache_file = self.cache_dir / f"{key}.json"

        if not cache_file.exists():
            return None

        with open(cache_file, "r", encoding="utf-8") as f:
            data = json.load(f)

        # TTL 확인
        cached_time = datetime.fromisoformat(data["timestamp"])
        if datetime.now() - cached_time > self.ttl:
            cache_file.unlink()
            return None

        return data["response"]

    def set(self, question: str, response: str, context: str = ""):
        """캐시에 저장"""
        key = self._get_key(question, context)
        cache_file = self.cache_dir / f"{key}.json"

        data = {
            "question": question,
            "response": response,
            "context": context,
            "timestamp": datetime.now().isoformat()
        }

        with open(cache_file, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False)


# 사용
cache = ResponseCache()


class ProductChatbot:
    def chat(self, question: str) -> str:
        # 캐시 확인
        cached = cache.get(question)
        if cached:
            return cached

        # LLM 호출
        response = self._llm_call(question)

        # 캐시 저장
        cache.set(question, response)

        return response
