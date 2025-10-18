from fastapi import APIRouter
from src.integrations.n8n_integration.schemas import WhatsAppMessageSchema
import requests

n8n_router = APIRouter()


@n8n_router.post(
    path = f"/message-doubts-agents-trigger",
)
async def send_message_doubts_agents_trigger(
    message: WhatsAppMessageSchema
) -> dict:
    """Send a message to the doubts Agent at N8N

    Args:
        message (WhatsAppMessageSchema): BaseModel with the message and the recipient phone number

    Returns:
        dict: Response from N8N
    """
    url = "https://test.buzzyai.com.br/webhook-test/message-doubts-agent"
    response = requests.post(
        url = url,
        json = message.model_dump(),
    )
    return response.json()

   