try:
    response = requests.get(url, timeout=10)
    response.raise_for_status()  # HTTP 에러 체크
except requests.RequestException as e:
    print(f"요청 실패: {e}")
