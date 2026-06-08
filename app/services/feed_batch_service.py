from app.ai.feed_classifier import classify_post
from app.ranking.feed_ranker import calculate_importance
from app.services.feed_digest_service import generate_digest
from app.services.post_service import (
    save_post,
    post_exists
)
from app.telegram.telegram_service import (
    send_telegram_message
)
from app.ai.feed_enricher import enrich_post


def process_batch(posts):

    important_posts = []

    for post in posts:

        category = classify_post(
            post.content
        )

        importance = calculate_importance(
            post.content
        )

        if importance >= 70:

            if not post_exists(
                post.content
            ):

                save_post(
                    author=post.author,
                    content=post.content,
                    category=category,
                    importance_score=importance
                )

                enriched = enrich_post(
                    post.content
                )

                summary = enriched["summary"]

                why_it_matters = (
                    enriched["why_it_matters"]
                )

                message = (
                    f"🚨 VEERA ALERT\n\n"
                    f"Category: {category}\n\n"
                    f"Author: {post.author}\n\n"
                    f"Importance Score: {importance}\n\n"

                    f"📌 Summary:\n"
                    f"{summary}\n\n"

                    f"💡 Why It Matters:\n"
                    f"{why_it_matters}"
                )

                send_telegram_message(
                    message
                )

            important_posts.append({
                "author": post.author,
                "category": category,
                "importance_score": importance,
                "content": post.content,
                "post_url": post.post_url
            })

    important_posts.sort(
        key=lambda x: x["importance_score"],
        reverse=True
    )

    return generate_digest(
        important_posts
    )