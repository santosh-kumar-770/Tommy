from fastapi import APIRouter
from app.schemas.linkedin_schema import LinkedInPost
from app.services.linkedin_service import process_post

router = APIRouter()

@router.post("/feed")
def receive_feed(post: LinkedInPost):
    return process_post(post)