from app.database.database import SessionLocal
from app.database.models import Post


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