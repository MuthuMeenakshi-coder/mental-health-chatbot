from fastapi import FastAPI
from pydantic import BaseModel
import openai
from fastapi.middleware.cors import CORSMiddleware

# Load OpenAI API key
openai.api_key = "your_openai_api_key"

app = FastAPI()

# Allow frontend to communicate with backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ChatRequest(BaseModel):
    message: str

@app.post("/chat")
async def chat(request: ChatRequest):
    """Handles user messages and returns AI-generated responses."""
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "system", "content": "You are a supportive mental health chatbot."},
                  {"role": "user", "content": request.message}]
    )
    return {"response": response["choices"][0]["message"]["content"]}

# Run with: uvicorn chatbot_backend:app --reload