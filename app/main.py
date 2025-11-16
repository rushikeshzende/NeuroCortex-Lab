from fastapi import FastAPI
from pydantic import BaseModel
from app.router import route_message

app = FastAPI(title="NeuroCortex Router")

class Message(BaseModel):
    message: str
    history: list = []

@app.post("/chat")
async def chat(req: Message):
    return await route_message(req.message, req.history)

@app.get("/health")
async def health():
    return {"status": "OK"}
