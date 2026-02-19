from chatbot import ProductChatbot


def main():
    chatbot = ProductChatbot()

    print("=" * 50)
    print("     🛒 상품 비교 챗봇")
    print("=" * 50)
    print("/help로 명령어를 확인하세요.")
    print("테스트 상품을 추가하려면 /test를 입력하세요.")
    print("종료하려면 /quit을 입력하세요.")
    print("=" * 50)
    print()

    while True:
        try:
            user_input = input("👤 You: ").strip()

            if not user_input:
                continue

            if user_input.lower() == "/quit":
                print("안녕히 가세요! 👋")
                break

            if user_input.lower() == "/test":
                print(chatbot.add_test_products())
                continue

            response = chatbot.process(user_input)
            print(f"\n🤖 AI: {response}\n")

        except KeyboardInterrupt:
            print("\n\n안녕히 가세요! 👋")
            break
        except Exception as e:
            print(f"오류 발생: {e}")


if __name__ == "__main__":
    main()
