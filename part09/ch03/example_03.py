import logging
from datetime import datetime

logger = logging.getLogger(__name__)


class ProductChatbot:
    def __init__(self):
        logger.info("챗봇 초기화")
        self.store = ProductStore()
        self.analyzer = ProductAnalyzer()
        self.request_count = 0

    def process(self, user_input: str, session_id: str = "default") -> str:
        """사용자 입력 처리"""
        self.request_count += 1
        start_time = datetime.now()

        logger.info(f"[{session_id}] 요청 #{self.request_count}: {user_input[:50]}...")

        try:
            if user_input.startswith("/"):
                response = self._handle_command(user_input)
            else:
                response = self.chat(user_input, session_id)

            elapsed = (datetime.now() - start_time).total_seconds()
            logger.info(f"[{session_id}] 응답 완료 ({elapsed:.2f}초)")

            return response

        except Exception as e:
            logger.error(f"[{session_id}] 처리 실패: {e}", exc_info=True)
            return "처리 중 오류가 발생했습니다."
