# models/models.py
from sqlalchemy import Column, Integer, String, JSON, DateTime
from sqlalchemy.sql import func
from database import Base

class ConversationModel(Base):
    __tablename__ = "conversations"  # Database table name
    
    id = Column(Integer, primary_key=True, index=True)  # Primary key column
    session_id = Column(String, unique=True, index=True)  # Session ID column (unique)
    title = Column(String)  # Title of the conversation
    messages = Column(JSON)  # Messages stored as a JSON object
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
