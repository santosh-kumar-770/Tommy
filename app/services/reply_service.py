from app.ai.reply_generator import generate_replies


def build_conversation(conversation):

    conversation_text = ""

    for msg in conversation:
        conversation_text += (
            f"{msg.sender}: {msg.message}\n"
        )

    return conversation_text


def suggest_replies(data):

    conversation_text = build_conversation(
        data.conversation
    )

    replies = generate_replies(
        conversation_text
    )

    # Convert AI response into a clean list
    reply_list = []

    for line in replies.split("\n"):

        line = line.strip()

        if not line:
            continue

        # Remove labels like Reply 1:, Reply 2:, etc.
        if ":" in line and line.lower().startswith("reply"):
            line = line.split(":", 1)[1].strip()

        reply_list.append(line)

    return {
        "person": data.person_name,
        "suggestions": reply_list[:3]
    }