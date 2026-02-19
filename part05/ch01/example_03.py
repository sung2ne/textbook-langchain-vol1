for msg in conversation:
    role = msg.__class__.__name__
    content = msg.content[:50] + "..." if len(msg.content) > 50 else msg.content
    print(f"[{role}] {content}")
