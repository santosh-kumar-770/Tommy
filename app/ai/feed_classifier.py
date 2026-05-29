def classify_post(content: str) -> str:
    content = content.lower()

    if "hackathon" in content:
        return "#hackathonalert"

    if "internship" in content:
        return "#internshipalert"

    if "event" in content:
        return "#eventupdates"

    if "openai" in content or "model" in content:
        return "#newmodelalert"

    if "hiring" in content or "opportunity" in content:
        return "#opportunityalert"

    return "#founderpost"