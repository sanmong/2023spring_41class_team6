from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class DocumentsSchema(BaseModel):
    docid: Optional[int]
    contents: str
    date: datetime
    source: str

    class config:
        orm_mode = True

class ChatroomSchema(BaseModel):
    chatroom_id: Optional[int]
    chat_start: datetime
    