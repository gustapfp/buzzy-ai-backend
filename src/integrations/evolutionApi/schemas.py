from pydantic import BaseModel

class BaseWhatsAppMessage(BaseModel):
    id: str
    name: str
    sender_phone_number: str
class WhatsAppTextMessage(BaseWhatsAppMessage):
    text_json: dict
    text: str

class WhatsAppAudioMessage(BaseWhatsAppMessage):
    audio_base64: str
    audio_json: dict

class WhatsAppImageMessage(BaseWhatsAppMessage):
    image_base64: str
    image_json: dict