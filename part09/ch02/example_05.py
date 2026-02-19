import os

# Streamlit Secrets 또는 환경 변수
MODEL_NAME = os.getenv("LLM_MODEL", "llama4")
DATA_FILE = os.getenv("DATA_FILE", "products.json")
