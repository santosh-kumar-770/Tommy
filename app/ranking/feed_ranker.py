def calculate_importance(content: str) -> int:
    content = content.lower()

    score = 50

    keywords = {
        "hackathon": 20,
        "internship": 15,
        "openai": 25,
        "ai": 15,
        "event": 15,
        "founder": 10,
        "startup": 10,
        "hiring": 15,
        "opportunity": 20,
        "model": 20
    }

    for keyword, points in keywords.items():
        if keyword in content:
            score += points

    return min(score, 100)