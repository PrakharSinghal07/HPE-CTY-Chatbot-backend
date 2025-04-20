from pydantic import BaseModel
from typing import List


class ChatRequest(BaseModel):
  query: str


class ChatResponse(BaseModel):
  response: str


class Suggestions(BaseModel):
  Suggestions: List[str]

class Conversation(BaseModel):
  messages: List[dict]
  sessionId: str
  title: str
  