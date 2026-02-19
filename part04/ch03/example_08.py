primary_chain = primary_llm | parser
fallback_chain = fallback_llm | parser

# primary가 실패하면 fallback 실행
chain = primary_chain.with_fallbacks([fallback_chain])
