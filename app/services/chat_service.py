from app.agent.agent import commerce_agent
from app.models.chat_models import ChatRequest, ChatResponse


class ChatService:

    async def chat(
        self,
        request: ChatRequest,
    ) -> ChatResponse:

        result = await commerce_agent.run(
            request.message
        )

        return ChatResponse(
            response=result["response"],
            tool_calls=result.get("tool_calls"),
        )


chat_service = ChatService()