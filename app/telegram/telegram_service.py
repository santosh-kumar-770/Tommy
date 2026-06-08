import requests

BOT_TOKEN = "8421814633:AAGc7Hc3UD_JKKIcLaUS_2P6uMufQn9qWDE"
CHAT_ID = "8868383062"


def send_telegram_message(message):

    url = (
        f"https://api.telegram.org/bot"
        f"{BOT_TOKEN}/sendMessage"
    )

    payload = {
        "chat_id": CHAT_ID,
        "text": message
    }

    response = requests.post(
        url,
        json=payload
    )

    print(response.text)

    return response.json()