from fastapi import APIRouter

from app.database.database import SessionLocal
from app.database.models import Post

router = APIRouter()


@router.get("/posts")
def get_posts():

    db = SessionLocal()

    posts = db.query(Post).all()

    result = []

    for post in posts:

        result.append({
            "id": post.id,
            "author": post.author,
            "category": post.category,
            "importance_score": post.importance_score,
            "content": post.content
        })

    db.close()

    return result