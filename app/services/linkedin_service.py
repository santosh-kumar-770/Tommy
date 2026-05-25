def process_post(post):
    return {
        "message": "Post received successfully",
        "author": post.author,
        "content": post.content
    }