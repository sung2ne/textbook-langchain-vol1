import requests
from typing import Optional

def safe_api_call(url: str, timeout: int = 10) -> Optional[dict]:
    """안전한 API 호출"""
    try:
        response = requests.get(url, timeout=timeout)
        response.raise_for_status()  # HTTP 에러 체크
        return response.json()
    except requests.Timeout:
        print("요청 시간 초과")
        return None
    except requests.HTTPError as e:
        print(f"HTTP 에러: {e}")
        return None
    except requests.RequestException as e:
        print(f"요청 실패: {e}")
        return None
    except ValueError:
        print("JSON 파싱 실패")
        return None


def get_data_with_fallback(url: str, fallback_data: dict) -> dict:
    """실패 시 기본값 반환"""
    data = safe_api_call(url)
    if data is None:
        return fallback_data
    return data


# 사용
fallback = {"temp": 20, "description": "정보 없음"}
weather = get_data_with_fallback("https://api.example.com/weather", fallback)
