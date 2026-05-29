def generate_summary(category: str, content: str) -> str:

    if category == "#newmodelalert":
        return f"""
#newmodelalert

{content[:120]}

Why it matters:
This update may impact AI developers and builders.
"""

    if category == "#hackathonalert":
        return f"""
#hackathonalert

{content[:120]}

Why it matters:
Potential opportunity for learning, networking and projects.
"""

    if category == "#internshipalert":
        return f"""
#internshipalert

{content[:120]}

Why it matters:
Potential internship opportunity for students.
"""

    if category == "#eventupdates":
        return f"""
#eventupdates

{content[:120]}

Why it matters:
Could be useful for networking and learning.
"""

    if category == "#opportunityalert":
        return f"""
#opportunityalert

{content[:120]}

Why it matters:
Potential career or growth opportunity.
"""

    return f"""
#founderpost

{content[:120]}

Why it matters:
Insights from a founder's experience.
"""