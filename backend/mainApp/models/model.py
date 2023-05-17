from sqlalchemy import Column, Integer, Date, DateTime, Text, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Documents(Base):
    __tablename__ = "documents"
    docid = Column(Integer, primary_key=True, nullable=False)
    contents = Column(Text, nullable=False)
    date = Column(Date)
    source = Column(Text)

class Chatroom(Base):
    chatroom_id = Column(Integer, primary_key=True, nullable=False)
    chat_start = Column(DateTime, nullable=False)
    last_interaction = Column(DateTime, nullable=False)

class Individual_chats(Base):
    chat_id = Column(Integer, primary_key=True, nullable=False)
    chatroom_id = Column(Integer, ForeignKey("Chatroom.chatroom_id", ondelete="CASCADE"), nullable=False)
    chatroom = relationship("Chatroom")
    order = Column(Integer, nullable=False)
    is_system = Column(Boolean, nullable=False)
    docid = Column(Integer, ForeignKey("Documents.docid", ondelete="CASCADE"), nullable=False)
    doc = relationship("Documents")
