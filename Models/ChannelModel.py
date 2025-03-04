from pydantic import BaseModel

from typing import List

from .MessageModel import Message

class Channel(BaseModel):
    channel_id: str
    ttl: int
    messages: List[Message]

class ChannelRequest(BaseModel):
    pass

class ChannelResponse(BaseModel):
    channel_id: str
    ttl: int