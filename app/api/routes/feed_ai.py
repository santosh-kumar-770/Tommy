from fastapi import APIRouter
from app.schemas.linkedin_schema import LinkedInPost
from app.ai.llm_feed_analyzer import analyze_post

router = APIRouter()


@router.post("/feed-ai")
def analyze_feed(post: LinkedInPost):

    result = analyze_post(
        post.content
    )

    return {
        "author": post.author,
        **result
    }