from fastapi import APIRouter
from models.schemas import Conversation
from typing import Optional, List

router = APIRouter(prefix="/conversation", tags=["Chatbot"])

# In-memory store for a single conversation
conversationObj = {}
conversationsArr = []

# POST a single conversation (save current chat session)
@router.post("/")
def save_conversation(conversation: Conversation):
    global conversationObj
    if not conversation.messages:
        return {"error": "Conversation must have messages."}
    
    # Save the incoming conversation object
    conversationObj = conversation
    print("Saved Conversation:")
    print(conversationObj)
    return {"message": "Conversation saved", "conversation": conversationObj}

# GET the last saved conversation (resume session)
@router.get("/")
def get_conversation():
    global conversationObj
    if not conversationObj:
        return {"error": "No conversation found. Start a new session."}
    
    print("Fetching Conversation:")
    print(conversationObj)
    return conversationObj


@router.post('/all')
def post_conversations(conversations: List[Conversation]):
    global conversationsArr
    # Filter out empty message convos
    filtered = [c for c in conversations if c.messages]
    if not filtered:
        return {"error": "No valid conversations to save."}
    conversationsArr = filtered
    print(conversationsArr)
    return conversationsArr


@router.get('/all')
def getConversations():
  global conversationsArr
  return conversationsArr