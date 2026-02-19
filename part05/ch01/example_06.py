import json
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage

def save_conversation(memory, filepath):
    data = []
    for msg in memory.get_messages():
        data.append({
            "type": msg.__class__.__name__,
            "content": msg.content
        })

    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def load_conversation(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        data = json.load(f)

    messages = []
    for item in data:
        if item["type"] == "SystemMessage":
            messages.append(SystemMessage(content=item["content"]))
        elif item["type"] == "HumanMessage":
            messages.append(HumanMessage(content=item["content"]))
        elif item["type"] == "AIMessage":
            messages.append(AIMessage(content=item["content"]))

    return messages

# 저장
save_conversation(memory, "conversation.json")

# 복원
loaded_messages = load_conversation("conversation.json")
