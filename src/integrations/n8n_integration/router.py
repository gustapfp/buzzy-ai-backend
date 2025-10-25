from fastapi import APIRouter
from src.agents.state_classifier.schemas import MessageClassification

import requests

from src.integrations.evolutionApi.schemas import WhatsAppTextMessage

n8n_router = APIRouter()


@n8n_router.post(
    path = "/send-message-to-agent",
    tags = ["N8N Integration"],
    summary = "Send a message to an agent at N8N.",
)
async def send_message_to_agent(
    classification: MessageClassification, 
    whatsapp_message: WhatsAppTextMessage,
    url: str
) -> dict:
    """Send a message to the doubts Agent at N8N

    Args:
        message (WhatsAppMessageSchema): BaseModel with the message and the recipient phone number

    Returns:
        dict: Response from N8N
    """

    response = requests.post(
        url = url,
        json = {
            "classification": classification.model_dump(),
            "whatsapp_info": whatsapp_message.model_dump(),
        },
    )
    return response.json()

   