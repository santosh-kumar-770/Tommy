from app.database.database import SessionLocal
from app.database.models import Post


def post_exists(content):

    db = SessionLocal()

    post = (
        db.query(Post)
        .filter(
            Post.content == content
        )
        .first()
    )

    db.close()

    return post is not None


def save_post(
    author,
    content,
    category,
    importance_score
):

    db = SessionLocal()

    post = Post(
        author=author,
        content=content,
        category=category,
        importance_score=importance_score
    )

    db.add(post)
    db.commit()
    db.refresh(post)

    db.close()

    return post