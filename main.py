from fastapi import FastAPI, Request
from pydantic import BaseModel
import requests

app = FastAPI()

# رابط سيرفرك المحلي عبر ngrok
LOCAL_MODEL_URL = "https://951f-156-203-135-116.ngrok-free.app/infer"

class ChatRequest(BaseModel):
    prompt: str

@app.post("/chat")
async def chat(req: ChatRequest):
    print(f"Received prompt: {req.prompt}")
    response = requests.post(LOCAL_MODEL_URL, json={"prompt": req.prompt})
    print(f"Local model response: {response.text}")
    return response.json()
