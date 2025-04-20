from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import chat, suggestions, conversation
import os
from dotenv import load_dotenv

load_dotenv()
frontendURL = os.getenv("FRONTEND_URL")
app = FastAPI()
origins = [
    frontendURL,
]

# Apply CORS settings
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # Allow your frontend's origin
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods (GET, POST, etc.)
    allow_headers=["*"],  # Allow all headers
)
app.include_router(chat.router) # pending
app.include_router(suggestions.router) # pending
app.include_router(conversation.router) # pending