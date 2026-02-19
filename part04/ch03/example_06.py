from langchain_core.runnables import RunnableLambda

def conditional_step(inputs):
    # 긴 텍스트만 요약
    if len(inputs["text"]) > 1000:
        return summarize_chain.invoke(inputs)
    return inputs["text"]

chain = RunnableLambda(conditional_step)
