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
    print(f"[Railway /chat] Received prompt: {req.prompt}")
    try:
        response = requests.post(LOCAL_MODEL_URL, json={"prompt": req.prompt}, timeout=10)
        print(f"[Railway /chat] Response status: {response.status_code}")
        print(f"[Railway /chat] Response body: {response.text}")
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"[Railway /chat] Error calling local model: {e}")
        return {"error": "Failed to reach local model."}
