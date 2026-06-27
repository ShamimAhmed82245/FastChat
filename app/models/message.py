from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime
from sqlalchemy.sql import func
from app.db.database import Base

class Message(Base):
    __tablename__ = "messages"

    id = Column(Integer, primary_key=True)

    conversation_id = Column(
        Integer, 
        ForeignKey("conversations.id", ondelete="CASCADE")
        )
    sender_id = Column(
        Integer,
        ForeignKey("users.id", ondelete = "CASCADE")
    )
    content = Column(Text, nullable = False)
    created_at = Column(DateTime, server_default=func.now())