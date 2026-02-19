import json
from pathlib import Path
from collections import Counter
from datetime import datetime


def show_dashboard():
    """로그 대시보드"""
    log_dir = Path("logs")

    print("=== 📊 대시보드 ===\n")

    # 오늘 로그
    date_str = datetime.now().strftime("%Y-%m-%d")
    log_file = log_dir / f"requests_{date_str}.jsonl"

    if not log_file.exists():
        print("오늘 로그가 없습니다.")
        return

    requests = []
    with open(log_file, "r", encoding="utf-8") as f:
        for line in f:
            requests.append(json.loads(line))

    print(f"오늘 요청 수: {len(requests)}")

    # 세션별 통계
    sessions = Counter(r["session_id"] for r in requests)
    print(f"활성 세션: {len(sessions)}")

    # 평균 길이
    avg_input = sum(r["input_length"] for r in requests) / len(requests)
    avg_output = sum(r["response_length"] for r in requests) / len(requests)
    print(f"평균 입력 길이: {avg_input:.0f}자")
    print(f"평균 출력 길이: {avg_output:.0f}자")

    # 최근 요청
    print("\n--- 최근 5개 요청 ---")
    for r in requests[-5:]:
        print(f"[{r['timestamp'][:19]}] {r['input'][:30]}...")


if __name__ == "__main__":
    show_dashboard()
