from fastapi import APIRouter

from src.integrations.evolutionApi.schemas import WhatsAppMessage


evolutionApi = APIRouter()

@evolutionApi.post(
    path = f"/messages-webhook",
    summary = "Webhook to receive the WhatsApp messages from Evolution API.",
    tags = ["Evolution API"],
)
async def messages_webhook(
    message: dict
) -> dict:
    """Webhook to receive the WhatsApp messages from Evolution API.

    Args:
        message (WhatsAppMessage): WhatsApp message received from Evolution API.

    Returns:
        dict: 
    """
    print(message)
    return {"message": message}
