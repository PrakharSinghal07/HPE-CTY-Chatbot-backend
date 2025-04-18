from fastapi import FastAPI
from routers import chat, suggestions

app = FastAPI()

app.include_router(chat.router) # pending
app.include_router(suggestions.router) # pending