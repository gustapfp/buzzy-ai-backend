from fastapi import APIRouter, HTTPException, status
from structlog import get_logger

from src.integrations.Integration_handler import IntegrationHandler
from src.integrations.evolutionApi.utils import WhatsAppMessageProcessor


evolutionApi = APIRouter()
processor = WhatsAppMessageProcessor()
logger = get_logger()
integration_handler = IntegrationHandler()

@evolutionApi.post(
    path = f"/messages-webhook",
    summary = "Webhook to receive the WhatsApp messages from Evolution API.",
    tags = ["Evolution API"],
)
async def messages_webhook(
    message: dict
) -> dict:
    """Webhook to receive the WhatsApp messages from Evolution API and extract the important payload
    information to be use by the agents.

    Args:
        message (EvolutionApiPayload): WhatsApp message received from Evolution API.

    Returns:
        dict: Processed message.
    """
    try: 
        processed_message = processor.process_whatsapp_message(message)
        if not processed_message:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, 
                detail="Unknown message type - should be: textMessage, imageMessage, or audioMessage")
        logger.info(f"Processed message: {processed_message}")
        await integration_handler.send_to_agent(processed_message)
        return {"message": processed_message}
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, 
            detail=f"Error processing message: {e}")


 
