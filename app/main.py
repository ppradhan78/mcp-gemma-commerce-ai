from fastapi import FastAPI

from app.models.chat_models import ChatRequest, ChatResponse
from app.services.chat_service import chat_service


app = FastAPI(
    title="MCP Gemma Commerce AI",
    version="1.0.0",
)


@app.get("/health")
async def health() -> dict:

    return {
        "status": "healthy",
        "service": "mcp-gemma-commerce-ai",
    }


@app.post(
    "/api/v1/chat",
    response_model=ChatResponse,
)
async def chat(
    request: ChatRequest,
) -> ChatResponse:

    return await chat_service.chat(request)