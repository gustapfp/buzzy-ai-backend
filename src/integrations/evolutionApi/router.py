from fastapi import APIRouter


from src.integrations.evolutionApi.utils import WhatsAppMessageProcessor


evolutionApi = APIRouter()
processor = WhatsAppMessageProcessor()

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
        message (EvolutionApiPayload): WhatsApp message received from Evolution API.

    Returns:
        dict: Processed message.
    """
    print(message)
    processed_message = processor.process_whatsapp_message(message)
    return {"message": processed_message.model_dump()}
