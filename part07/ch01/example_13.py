def inspect_documents(documents: list, max_chars: int = 100):
    """문서 목록 확인"""
    print(f"총 {len(documents)}개 문서\n")

    for i, doc in enumerate(documents[:5]):  # 처음 5개만
        content_preview = doc.page_content[:max_chars]
        if len(doc.page_content) > max_chars:
            content_preview += "..."

        print(f"[문서 {i+1}]")
        print(f"출처: {doc.metadata.get('source', 'N/A')}")
        print(f"내용: {content_preview}")
        print()


# 사용
inspect_documents(documents)
