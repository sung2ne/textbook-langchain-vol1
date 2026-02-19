import streamlit as st

def stream_chat(question: str):
    """Streamlit 스트리밍"""
    response_placeholder = st.empty()
    full_response = ""

    for chunk in chain.stream({"question": question}):
        content = chunk.content if hasattr(chunk, 'content') else str(chunk)
        full_response += content
        response_placeholder.markdown(full_response + "▌")

    response_placeholder.markdown(full_response)
    return full_response
