import ollama


def generate_replies(conversation_text: str):

    prompt = f"""
You are a LinkedIn assistant.

Task:
Generate exactly 3 reply suggestions.

IMPORTANT RULES:
- Return only the replies.
- No explanations.
- No introductions.
- No analysis.
- No roleplay.
- No labels.
- No numbering.
- Each reply must be on a new line.
- Professional tone.
- Simple English.
- Maximum 20 words per reply.

Conversation:

{conversation_text}

Replies:
"""

    response = ollama.chat(
        model="llama3.2:1b",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response["message"]["content"]