import os

def create_sample_knowledge_base(base_dir: str):
    """샘플 지식 베이스 생성"""

    structure = {
        "company": {
            "about.txt": """
회사 소개

ABC 테크는 2010년에 설립된 AI 전문 기업입니다.
본사는 서울 강남구에 위치하고 있습니다.
현재 직원 수는 150명입니다.

주요 사업 분야:
- AI 솔루션 개발
- 클라우드 서비스
- 데이터 분석 플랫폼
""",
            "products.txt": """
제품 소개

1. AI Assistant Pro
- 기업용 AI 어시스턴트
- 가격: 월 99,000원
- 주요 기능: 문서 분석, 자동 응답, 업무 자동화

2. DataCloud
- 클라우드 데이터 저장 서비스
- 가격: 용량에 따라 책정
- 주요 기능: 자동 백업, 실시간 동기화

3. Analytics Hub
- 데이터 분석 플랫폼
- 가격: 월 199,000원
- 주요 기능: 대시보드, 리포트 생성, AI 예측
""",
            "contact.txt": """
연락처 정보

대표전화: 02-1234-5678
팩스: 02-1234-5679
이메일: contact@abctech.com

고객센터 운영시간:
- 평일: 09:00 - 18:00
- 주말/공휴일: 휴무

기술 지원:
- 이메일: support@abctech.com
- 긴급 연락: 010-1234-5678 (24시간)
"""
        },
        "policies": {
            "privacy.txt": """
개인정보 처리방침

1. 수집하는 개인정보
- 이름, 이메일, 전화번호
- 서비스 이용 기록

2. 개인정보 이용 목적
- 서비스 제공
- 고객 지원
- 마케팅 (동의 시)

3. 개인정보 보관 기간
- 회원 탈퇴 시까지
- 법령에 따른 보관 의무 기간

4. 개인정보 삭제
- 탈퇴 요청 시 즉시 삭제
- support@abctech.com으로 요청
""",
            "refund.txt": """
환불 정책

1. 환불 조건
- 결제 후 7일 이내
- 서비스 미사용 시

2. 환불 방법
- 고객센터 연락
- 이메일로 환불 요청서 제출

3. 환불 처리 기간
- 신청 후 영업일 기준 3-5일

4. 부분 환불
- 월간 요금제: 미사용 기간 일할 계산
- 연간 요금제: 사용 월 제외 환불
"""
        },
        "guides": {
            "getting_started.txt": """
시작하기 가이드

1. 회원가입
- 웹사이트 접속: www.abctech.com
- 이메일 인증

2. 제품 선택
- 무료 체험 가능 (14일)
- 요금제 비교 후 선택

3. 초기 설정
- 프로필 설정
- 팀원 초대 (Pro 플랜)
- API 키 발급

4. 도움이 필요하면
- 가이드 문서: docs.abctech.com
- 고객센터: 02-1234-5678
""",
            "faq.txt": """
자주 묻는 질문

Q: 무료 체험 기간은 얼마인가요?
A: 14일간 모든 기능을 무료로 사용할 수 있습니다.

Q: 결제 방법은 무엇인가요?
A: 신용카드, 계좌이체, 페이팔을 지원합니다.

Q: 팀원 추가 비용이 있나요?
A: Pro 플랜은 5명까지 무료, 추가 인원당 월 10,000원입니다.

Q: 데이터 백업은 어떻게 하나요?
A: 자동으로 매일 백업됩니다. 수동 백업도 가능합니다.

Q: 해지하면 데이터는 어떻게 되나요?
A: 해지 후 30일간 보관 후 삭제됩니다. 미리 내보내기하세요.
"""
        }
    }

    for category, files in structure.items():
        dir_path = os.path.join(base_dir, category)
        os.makedirs(dir_path, exist_ok=True)

        for filename, content in files.items():
            file_path = os.path.join(dir_path, filename)
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(content.strip())

    print(f"지식 베이스 생성 완료: {base_dir}")


# 샘플 생성
create_sample_knowledge_base("./knowledge_base/")
