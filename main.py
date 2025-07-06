from fastapi import FastAPI
from pydantic import BaseModel
import requests

app = FastAPI()

# رابط السيرفر المحلي عبر ngrok (احذف المسافة في البداية!)
LOCAL_MODEL_URL = "https://b85c-156-203-135-116.ngrok-free.app/infer"

class ChatRequest(BaseModel):
    prompt: str

@app.post("/chat")
async def chat(req: ChatRequest):
    prompt = req.prompt.strip()
    print(f"[Render /chat] Received prompt: {prompt}")

    try:
        response = requests.post(LOCAL_MODEL_URL, json={"prompt": prompt}, timeout=10)
        print(f"[Render /chat] Response status: {response.status_code}")
        print(f"[Render /chat] Response body: {response.text}")
        response.raise_for_status()
        return response.json()

    except requests.exceptions.Timeout:
        return {"error": "Request to local model timed out."}
    except requests.exceptions.ConnectionError:
        return {"error": "Failed to connect to the local model. Check ngrok tunnel."}
    except requests.exceptions.RequestException as e:
        print(f"[Render /chat] Unexpected error: {e}")
        return {"error": "An unexpected error occurred when reaching the local model."}
