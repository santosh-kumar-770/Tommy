import ollama


def generate_replies(conversation_text: str):

    prompt = f"""
You are Veera AI.

Generate exactly 3 reply suggestions for LinkedIn.

Rules:
- Professional tone
- Simple English
- Friendly
- Short (1-2 sentences)
- Do not roleplay
- Do not mention Veera
- Do not mention Person
- Do not explain
- Do not number replies
- One reply per line

Conversation:

{conversation_text}
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