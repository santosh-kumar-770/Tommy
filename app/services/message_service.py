from app.database.database import SessionLocal
from app.database.models import Message


def save_message(
    person_name,
    sender,
    message
):

    db = SessionLocal()

    msg = Message(
        person_name=person_name,
        sender=sender,
        message=message
    )

    db.add(msg)

    db.commit()

    db.refresh(msg)

    db.close()

    return msg