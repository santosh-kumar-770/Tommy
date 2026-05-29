from app.ai.llm_feed_analyzer import analyze_post


def process_post(post):

    analysis = analyze_post(
        post.content
    )

    return {
        "status": "success",
        "author": post.author,
        **analysis
    }