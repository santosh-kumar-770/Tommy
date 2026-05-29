from pydantic import BaseModel
from typing import List, Optional


class FeedPost(BaseModel):
    author: str
    content: str
    post_url: Optional[str] = None


class FeedBatch(BaseModel):
    posts: List[FeedPost]