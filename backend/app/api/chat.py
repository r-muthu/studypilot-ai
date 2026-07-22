from fastapi import APIRouter

from app.agents.study_agent import study_agent
from app.agents.utils import get_agent_text
from app.schemas.chat import (
    ChatRequest,
    ChatResponse,
)

router = APIRouter(prefix="/chat", tags=["Chat"])


@router.post(
    "",
    response_model=ChatResponse,
)
async def chat(
    request: ChatRequest,
):
    config = {
        "configurable": {
            "thread_id": request.conversation_id,
        }
    }

    response = study_agent.invoke(
        {
            "messages": [
                {
                    "role": "user",
                    "content": request.message,
                }
            ]
        },
        config=config,
    )

    return ChatResponse(
        response=get_agent_text(
            response["messages"][-1]
        )
    )