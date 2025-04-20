from fastapi import APIRouter
from models.schemas import ChatRequest, ChatResponse
from services.llm_service import get_llm_response
router = APIRouter(prefix="/chat", tags=["Chatbot"])

@router.post("/", response_model=ChatResponse)
def get_chat_response(request: ChatRequest):
  response = get_llm_response(request.query)
  return {'response': response}