from app.ai.reply_generator import generate_replies
from app.services.memory_service import get_memory
from app.services.message_service import save_message

def build_conversation(conversation):

    conversation_text = ""

    for msg in conversation:
        conversation_text += (
            f"{msg.sender}: {msg.message}\n"
        )

    return conversation_text


def suggest_replies(data):

    # Load memory
    memory = get_memory(
        data.person_name
    )

    # Save previous topic before updating
    previous_topic = memory.last_topic

    # Build current conversation
    conversation_text = build_conversation(
        data.conversation
    )

    for msg in data.conversation:

        save_message(
            person_name=data.person_name,
            sender=msg.sender,
            message=msg.message
        )

    # IMPORTANT:
    # For now send ONLY conversation to AI.
    # Llama 3.2 1B gets confused by memory context.
    replies = generate_replies(
        conversation_text
    )

    # Parse replies
    reply_list = []

    for line in replies.split("\n"):

        line = line.strip()

        line = line.lstrip("1234567890.- ")

        if not line:
            continue

        # Remove Reply 1:, Reply 2:, etc.
        if (
            ":" in line
            and line.lower().startswith("reply")
        ):
            line = (
                line.split(":", 1)[1]
                .strip()
            )

        # Filter junk output
        blocked_phrases = [
            "person name",
            "relationship score",
            "conversation",
            "reply suggestions",
            "here are",
            "suggestions"
        ]

        should_skip = False

        for phrase in blocked_phrases:
            if phrase in line.lower():
                should_skip = True
                break

        if should_skip:
            continue

        if len(line) < 10:
            continue

        if len(line) > 150:
            continue

        reply_list.append(line)

    # Update memory
    if data.conversation:

        latest_message = (
            data.conversation[-1]
            .message
        )

        memory.last_topic = (
            latest_message[:100]
        )

        memory.previous_messages.append(
            latest_message
        )

    return {
        "person": data.person_name,
        "memory_loaded": True,
        "previous_topic": previous_topic,
        "current_topic": memory.last_topic,
        "suggestions": reply_list[:3]
    }