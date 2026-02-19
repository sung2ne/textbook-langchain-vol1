# 최근 10개 메시지만 유지
MAX_MESSAGES = 10

def chat_with_window(user_input):
    global conversation

    conversation.append(HumanMessage(content=user_input))

    # 시스템 메시지 + 최근 메시지만 선택
    system_msg = conversation[0]  # 시스템 메시지
    recent_msgs = conversation[-MAX_MESSAGES:]  # 최근 메시지

    if conversation[0] not in recent_msgs:
        messages_to_send = [system_msg] + recent_msgs
    else:
        messages_to_send = recent_msgs

    response = llm.invoke(messages_to_send)
    conversation.append(response)

    return response.content
