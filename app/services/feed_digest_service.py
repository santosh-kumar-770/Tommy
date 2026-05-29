from app.ai.feed_enricher import enrich_post


def generate_digest(posts):

    digest = []

    for post in posts:

        enriched = enrich_post(
            post["content"]
        )

        digest.append({
            **post,
            "ai_analysis": enriched
        })

    return digest