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
        WhatsAppTextMessage | WhatsAppAudioMessage | WhatsAppImageMessage | dict
    ):
       
        message_type = message.get("data", {}).get("messageType", "unknown")
        
        match message_type:
            case "extendedTextMessage":
                return self.__extract_text_message(message)
            case "conversation":
                return self.__extract_text_message(message)
            case "audioMessage":
                return self.__extract_audio_message(message)
            case "imageMessage":
                return self.__extract_image_message(message)
            case _:
                return {"message_type": "unknown", "message": message}
       
    def __extract_text_message(self, message: dict) -> WhatsAppTextMessage:
        data= message.get("data", {})
        logger.info(f"Extracting text message: {data}")
        try: 
            return WhatsAppTextMessage(
                id=data.get("key", {}).get("id", "unknown"),
                name=data.get("pushName", "unknown"),
                text_json=data.get("message", {}),
                sender_phone_number=self.transform.number_link_to_phone_number(message.get("sender"))
            )
        except Exception as e:
            raise WhatsAppMessageError(f"Error extracting text message: {e} - message: {message}")

    def __extract_audio_message(self, message: dict) -> WhatsAppAudioMessage:
        data= message.get("data", {})
        logger.info(f"Extracting audio message: {data}")
        try: 
            return WhatsAppAudioMessage(
                id=data.get("key", {}).get("id", "unknown"),
                name=data.get("pushName", "unknown"),
                audio_base64=data.get("message", {}).get("base64", ""),
                audio_json=data.get("message", {}).get("audioMessage", ""),
                sender_phone_number=self.transform.number_link_to_phone_number(message.get("sender"))
            )
        except Exception as e:
            raise WhatsAppMessageError(f"Error extracting audio message: {e} - message: {message}")
    
    def __extract_image_message(self, message: dict) -> WhatsAppImageMessage:
        data= message.get("data", {})
        logger.info(f"Extracting image message: {data}")
        try: 
            return WhatsAppImageMessage(
                id=data.get("key", {}).get("id", "unknown"),
                name=data.get("pushName", "unknown"),
                image_base64=data.get("message", {}).get("base64"),
                image_json=data.get("message", {}).get("imageMessage", {}),
                sender_phone_number=self.transform.number_link_to_phone_number(message.get("sender"))
            )
        except Exception as e:
            raise WhatsAppMessageError(f"Error extracting image message: {e} - message: {message}")
