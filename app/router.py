import httpx

MODEL_MAP = {
    "reasoning": "deepseek-r1:8b",
    "coding": "deepseek-coder:33b",
    "chat": "llama3:8b",
}

def classify_mode(message: str):
    m = message.lower()
    if "code" in m or "bug" in m:
        return "coding"
    if "explain" in m or "why" in m:
        return "reasoning"
    return "chat"

async def route_message(message, history):
    mode = classify_mode(message)
    model = MODEL_MAP.get(mode, "llama3:8b")

    async with httpx.AsyncClient() as client:
        r = await client.post(
            "http://localhost:11434/api/generate",
            json={"model": model, "prompt": message}
        )
        reply = r.json().get("response", "")

    return {
        "reply": reply,
        "model": model,
        "mode": mode
    }
