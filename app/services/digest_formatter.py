def format_digest(posts):

    digest = "🚀 VEERA DAILY DIGEST\n\n"

    for post in posts:

        digest += f"""
{post['category']}

Author: {post['author']}

{post['content']}

Importance Score: {post['importance_score']}

--------------------------------

"""

    return digest