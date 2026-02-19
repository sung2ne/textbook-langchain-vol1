# 소설처럼 읽는 LangChain과 생성형 AI 1권 - 실습 코드

[위키독스 교재](https://wikidocs.net/book/18963)의 실습 코드 저장소입니다.

Ollama와 LangChain으로 시작하는 생성형 AI 입문서로, 로컬 LLM 실행부터 체인 구성, 메모리, 웹 연동, 문서 처리까지 단계별로 학습합니다.

## 사용 방법

원하는 챕터의 브랜치를 체크아웃하면 해당 시점까지의 완성된 프로젝트를 받을 수 있습니다.

```bash
# 저장소 클론
git clone https://github.com/sung2ne/textbook-langchain-vol1.git
cd textbook-langchain-vol1

# 가상환경 생성 및 활성화
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate

# 의존성 설치
pip install -r requirements.txt

# 원하는 챕터로 이동
git checkout part05/chapter-02   # PART 05의 02장까지 완성된 코드
```

## 브랜치 목록

각 브랜치는 해당 챕터까지의 코드가 누적 적용되어 독립적으로 실행 가능합니다. 총 **36개** 브랜치가 제공됩니다.

> PART 01은 환경 설정 위주로 05장(OpenAI API 키 설정)만 브랜치가 있습니다. PART 02부터 본격적인 LangChain 코드가 시작됩니다.

### PART 01. 개발 환경 준비

| 브랜치 | 내용 |
|--------|------|
| `part01/chapter-05` | OpenAI API 키 설정 |

### PART 02. LLM의 세계로

| 브랜치 | 내용 |
|--------|------|
| `part02/chapter-02` | 토큰과 컨텍스트 |
| `part02/chapter-03` | 프롬프트의 기초 |
| `part02/chapter-04` | 모델 비교 |

### PART 03. LangChain 첫걸음

| 브랜치 | 내용 |
|--------|------|
| `part03/chapter-01` | LangChain 설치 |
| `part03/chapter-02` | 메시지와 시스템 프롬프트 |
| `part03/chapter-03` | 프롬프트 템플릿 |
| `part03/chapter-04` | 출력 파서 |

### PART 04. 체인의 세계

| 브랜치 | 내용 |
|--------|------|
| `part04/chapter-01` | LCEL 소개 |
| `part04/chapter-02` | Runnable 활용 |
| `part04/chapter-03` | 조건부 분기 |
| `part04/chapter-04` | 실용적인 체인 예시 |

### PART 05. 메모리와 대화

| 브랜치 | 내용 |
|--------|------|
| `part05/chapter-01` | 대화 기록 관리 |
| `part05/chapter-02` | ChatMessageHistory |
| `part05/chapter-03` | 메모리 전략 |
| `part05/chapter-04` | 챗봇 만들기 |

### PART 06. 웹과 연결하기

| 브랜치 | 내용 |
|--------|------|
| `part06/chapter-01` | 웹 페이지 가져오기 |
| `part06/chapter-02` | API 연동 |
| `part06/chapter-03` | 문서 처리 |
| `part06/chapter-04` | 실시간 정보 챗봇 |

### PART 07. 데이터와 연결하기

| 브랜치 | 내용 |
|--------|------|
| `part07/chapter-01` | 파일 로더 |
| `part07/chapter-02` | 문서 QA |
| `part07/chapter-03` | CSV와 구조화 데이터 |
| `part07/chapter-04` | 파일 기반 지식 베이스 |

### PART 08. 첫 번째 프로젝트

| 브랜치 | 내용 |
|--------|------|
| `part08/chapter-01` | 프로젝트 구조 |
| `part08/chapter-02` | 상품 정보 추출 |
| `part08/chapter-03` | 상품 분석 체인 |
| `part08/chapter-04` | 대화형 인터페이스 |
| `part08/chapter-05` | 프로젝트 완성 |

### PART 09. 배포와 운영

| 브랜치 | 내용 |
|--------|------|
| `part09/chapter-01` | CLI 도구 패키징 |
| `part09/chapter-02` | Streamlit 웹 UI |
| `part09/chapter-03` | 로깅과 모니터링 |
| `part09/chapter-04` | 성능 최적화 |

### PART 10. 다음 단계

| 브랜치 | 내용 |
|--------|------|
| `part10/chapter-01` | 1권 정리 |
| `part10/chapter-02` | 2권 미리보기 |
| `part10/chapter-03` | 학습 리소스 |

## 기술 스택

- **언어**: Python 3.11+
- **LLM 프레임워크**: LangChain 0.3.x
- **로컬 LLM**: Ollama (llama4)
- **클라우드 LLM**: OpenAI GPT-4o-mini
- **웹 UI**: Streamlit
- **문서 처리**: pypdf, BeautifulSoup4

## 실행 방법

```bash
# 의존성 설치
pip install -r requirements.txt

# OpenAI API 키 설정 (필요한 경우)
cp .env.example .env
# .env 파일에 OPENAI_API_KEY 입력

# Ollama 설치 및 모델 다운로드 (로컬 LLM 사용 시)
# https://ollama.com 에서 설치 후
ollama pull llama4

# 예제 실행
python example_01.py
```

## 라이선스

이 저장소는 [소설처럼 읽는 LangChain과 생성형 AI 1권](https://wikidocs.net/book/18963) 교재의 실습 코드입니다.
