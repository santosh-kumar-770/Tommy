from fastapi import APIRouter

from app.schemas.feed_batch_schema import FeedBatch
from app.services.feed_batch_service import process_batch

router = APIRouter()


@router.post("/feed-batch")
def analyze_feed_batch(data: FeedBatch):

    results = process_batch(
        data.posts
    )

    return {
        "important_posts": results,
        "count": len(results)
    }