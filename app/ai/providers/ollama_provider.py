import json
import ollama

from app.ai.providers.base_provider import BaseProvider


class OllamaProvider(BaseProvider):

    def analyze_feed(self, content: str):

        prompt = f"""
You are Veera AI.

Your job is to analyze LinkedIn posts.

Rules:
- Return ONLY valid JSON.
- Do not return markdown.
- Do not return explanations.
- Do not wrap JSON inside code blocks.
- importance_score must be between 0 and 100.
- why_it_matters must never be empty.
- summary must be concise and easy to understand.
- Choose exactly ONE category.

Allowed Categories:
#newmodelalert
#eventupdates
#hackathonalert
#internshipalert
#founderpost
#opportunityalert

LinkedIn Post:
{content}

Return JSON in exactly this format:

{{
    "category": "#founderpost",
    "importance_score": 50,
    "summary": "Short summary",
    "why_it_matters": "Why this matters to the user"
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

        raw_response = response["message"]["content"]

        try:
            data = json.loads(raw_response)

            if not data.get("why_it_matters"):
                data["why_it_matters"] = (
                    "Potentially useful update for professional growth."
                )

            if not data.get("importance_score"):
                data["importance_score"] = 50

            return data

        except Exception:

            return {
                "category": "#founderpost",
                "importance_score": 50,
                "summary": raw_response[:200],
                "why_it_matters": (
                    "AI response could not be parsed correctly."
                )
            }