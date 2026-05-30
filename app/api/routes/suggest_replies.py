from fastapi import APIRouter

from app.schemas.message_schema import ReplyRequest
from app.services.reply_service import suggest_replies

router = APIRouter()


@router.post("/suggest-replies")
def get_replies(data: ReplyRequest):

    return suggest_replies(data)