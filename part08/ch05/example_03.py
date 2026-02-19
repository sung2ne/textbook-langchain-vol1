import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)


class ProductChatbot:
    def process(self, user_input: str, session_id: str = "default") -> str:
        logger.info(f"Input: {user_input[:50]}...")
        response = self._process_internal(user_input, session_id)
        logger.info(f"Output: {response[:50]}...")
        return response
