import time

for url in urls:
    response = requests.get(url)
    # 처리...
    time.sleep(1)  # 1초 대기
