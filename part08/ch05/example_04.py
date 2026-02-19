# config.py
import os

CONFIG = {
    "model": os.getenv("LLM_MODEL", "llama4"),
    "data_file": os.getenv("DATA_FILE", "products.json"),
    "scraper_timeout": int(os.getenv("SCRAPER_TIMEOUT", "10")),
    "use_llm_scraper": os.getenv("USE_LLM_SCRAPER", "false").lower() == "true",
}
