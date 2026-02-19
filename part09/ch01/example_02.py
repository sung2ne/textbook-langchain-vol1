"""CLI 진입점"""

import argparse
import sys
from .chatbot import ProductChatbot


def main():
    parser = argparse.ArgumentParser(
        description="AI 기반 상품 비교 챗봇",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
예시:
  product-compare                  # 대화 모드 시작
  product-compare --test           # 테스트 데이터로 시작
  product-compare --version        # 버전 확인
        """
    )

    parser.add_argument(
        "--version", "-v",
        action="store_true",
        help="버전 정보 출력"
    )
    parser.add_argument(
        "--test", "-t",
        action="store_true",
        help="테스트 상품 데이터 추가"
    )
    parser.add_argument(
        "--data-file", "-d",
        type=str,
        default="products.json",
        help="상품 데이터 파일 경로 (기본: products.json)"
    )

    args = parser.parse_args()

    if args.version:
        from . import __version__
        print(f"product-compare-bot v{__version__}")
        sys.exit(0)

    # 챗봇 시작
    run_chatbot(args.test, args.data_file)


def run_chatbot(add_test: bool, data_file: str):
    """챗봇 실행"""
    chatbot = ProductChatbot(data_file=data_file)

    print("=" * 50)
    print("     🛒 상품 비교 챗봇")
    print("=" * 50)
    print("/help로 명령어를 확인하세요.")
    print("종료하려면 /quit을 입력하세요.")
    print("=" * 50)
    print()

    if add_test:
        print(chatbot.add_test_products())
        print()

    while True:
        try:
            user_input = input("👤 You: ").strip()

            if not user_input:
                continue

            if user_input.lower() in ["/quit", "/exit", "/q"]:
                print("안녕히 가세요! 👋")
                break

            response = chatbot.process(user_input)
            print(f"\n🤖 AI: {response}\n")

        except KeyboardInterrupt:
            print("\n\n안녕히 가세요! 👋")
            break
        except Exception as e:
            print(f"오류: {e}")


if __name__ == "__main__":
    main()
