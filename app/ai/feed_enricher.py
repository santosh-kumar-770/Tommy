import json
import ollama


def enrich_post(content: str):

    prompt = f"""
Create a short summary and explain why this matters.

Rules:
- Return ONLY valid JSON.
- No markdown.
- No code blocks.

Post:
{content}

Format:

{{
    "summary": "",
    "why_it_matters": ""
}}
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

    raw = response["message"]["content"]

    raw = raw.replace("```json", "")
    raw = raw.replace("```", "")
    raw = raw.strip()

    try:
        print("\nRAW OLLAMA RESPONSE:")
        print(raw)
        print("\n")
        return json.loads(raw)

    except Exception:

        return {
            "summary": content[:100],
            "why_it_matters": "Could not generate structured analysis."
        }