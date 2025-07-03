from fastapi import FastAPI, Request
from pydantic import BaseModel
import requests

app = FastAPI()

# رابط سيرفرك المحلي عبر ngrok
LOCAL_MODEL_URL = "https://a1b2c3.ngrok-free.app/infer"

class ChatRequest(BaseModel):
    prompt: str

@app.post("/chat")
async def chat(req: ChatRequest):
    # بعت الـ prompt للسيرفر المحلي
    response = requests.post(LOCAL_MODEL_URL, json={"prompt": req.prompt})
    return response.json()
