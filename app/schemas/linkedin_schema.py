from pydantic import BaseModel
from typing import Optional


class LinkedInPost(BaseModel):
    author: str
    content: str
    post_url: Optional[str] = None