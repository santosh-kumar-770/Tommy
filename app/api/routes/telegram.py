from fastapi import APIRouter

from app.telegram.telegram_service import (
    send_telegram_message
)

router = APIRouter()


@router.get("/test-alert")
def test_alert():

    return send_telegram_message(
        "🚀 Veera Telegram Integration Working!"
    )