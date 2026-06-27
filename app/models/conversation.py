from sqlalchemy import Column, Integer, Boolean, String
from app.db.database import Base

class Conversation(Base):
    __tablename__ = "conversations"

    id = Column(Integer, primary_key = True)
    is_group = Column(Boolean, default=False)
    name = Column(String, nullable=True)

    