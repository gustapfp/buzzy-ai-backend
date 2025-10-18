from typing import Any
from src.integrations.evolutionApi.schemas import WhatsAppAudioMessage, WhatsAppImageMessage, WhatsAppTextMessage
from src.integrations.evolutionApi.transformer import WhatsAppMessageTransformer
from structlog import get_logger
logger = get_logger()


class WhatsAppMessageError(Exception):
    """Exception raised when an error occurs while processing a WhatsApp message."""

class WhatsAppMessageProcessor: 
    def __init__(self):
        self.transform = WhatsAppMessageTransformer()

    def process_whatsapp_message(self, message: dict) -> Any:
        return self.__extract_message_based_on_type(message)

    def __extract_message_based_on_type(self, message: dict) -> (
        WhatsAppTextMessage | WhatsAppAudioMessage | WhatsAppImageMessage | None
    ):
        message_type = message.get("data", {}).get("message_type", "unknown")
        match message_type:
            case "extendedTextMessage":
                return self.__extract_text_message(message)
            case "audioMessage":
                return None
            case "imageMessage":
                return None
            case _:
                return None
       
    def __extract_text_message(self, message: dict) -> WhatsAppTextMessage:
        data= message.get("data", {})
        try: 
            return WhatsAppTextMessage(
                id=data.get("key", {}).get("id", "unknown"),
                name=data.get("pushName"),
                text_json=data.get("message"),
                sender_phone_number=self.transform.number_link_to_phone_number(message.get("sender"))
            )
        except Exception as e:
            raise WhatsAppMessageError(f"Error extracting text message: {e} - message: {message}")