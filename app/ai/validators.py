def validate_analysis(data):

    if not data.get("why_it_matters"):
        data["why_it_matters"] = (
            "Potentially useful update for professional growth."
        )

    if data.get("importance_score", 0) < 20:
        data["importance_score"] = 50

    return data