from pydantic import BaseModel
from typing import List


class ChatMessage(BaseModel):
    sender: str
    message: str


class ReplyRequest(BaseModel):
    person_name: str
    conversation: List[ChatMessage]