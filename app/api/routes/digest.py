from fastapi import APIRouter

from app.schemas.feed_batch_schema import FeedBatch
from app.services.feed_batch_service import process_batch
from app.services.digest_formatter import format_digest

router = APIRouter()


@router.post("/digest")
def generate_digest(data: FeedBatch):

    important_posts = process_batch(
        data.posts
    )

    digest = format_digest(
        important_posts
    )

    return {
        "digest": digest
    }