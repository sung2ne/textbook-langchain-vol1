def process(user_input):
    if user_input.startswith("/"):
        return handle_command(user_input)
    else:
        return chat(user_input)
