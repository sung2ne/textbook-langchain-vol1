from langchain_core.runnables import RunnableLambda

def safe_process(inputs):
    try:
        return risky_chain.invoke(inputs)
    except Exception as e:
        return f"처리 중 오류 발생: {e}"

safe_chain = RunnableLambda(safe_process)
