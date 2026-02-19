# 파이프라인 연결
chain = prompt | llm | parser

# 실행 방법
chain.invoke({"key": "value"})      # 단일 실행
chain.batch([{...}, {...}])          # 배치 실행
chain.stream({"key": "value"})       # 스트리밍
await chain.ainvoke({"key": "value"}) # 비동기
