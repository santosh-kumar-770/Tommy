from app.ai.feed_classifier import classify_post
from app.ranking.feed_ranker import calculate_importance
from app.services.feed_digest_service import generate_digest


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