from fastapi import APIRouter

from app.database.database import SessionLocal
from app.database.models import Message

router = APIRouter()


@router.get("/messages")
def get_messages():

    db = SessionLocal()

    messages = db.query(
        Message
    ).all()

    result = []

    for msg in messages:

        result.append({
            "id": msg.id,
            "person_name": msg.person_name,
            "sender": msg.sender,
            "message": msg.message
        })

    db.close()

    return result