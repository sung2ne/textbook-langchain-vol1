import logging

# 기본 설정
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)

# 사용
logger.info("애플리케이션 시작")
logger.warning("주의 메시지")
logger.error("오류 발생")
