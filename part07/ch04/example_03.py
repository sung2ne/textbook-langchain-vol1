def main():
    # 지식 베이스 초기화
    kb = KnowledgeBase("./knowledge_base/")

    print("=" * 50)
    print("     지식 베이스 챗봇")
    print("=" * 50)
    print(f"로드된 문서: {kb.get_stats()['total_documents']}개")
    print(f"카테고리: {list(kb.get_stats()['categories'].keys())}")
    print("=" * 50)
    print("명령어: /docs - 문서 목록, /quit - 종료\n")

    while True:
        user_input = input("👤 You: ").strip()

        if not user_input:
            continue
        elif user_input == "/quit":
            break
        elif user_input == "/docs":
            for doc in kb.list_documents():
                print(f"  - {doc}")
            continue

        response = kb.ask(user_input)
        print(f"🤖 AI: {response}\n")


if __name__ == "__main__":
    main()
