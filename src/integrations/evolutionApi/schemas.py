from pydantic import BaseModel


class WhatsAppTextMessage(BaseModel):
    id: str
    name: str
    text_json: dict
    sender_phone_number: str

class WhatsAppAudioMessage(BaseModel):
    id: str
    name: str
    audio_base64: str
    audio_json: dict
    sender_phone_number: str

class WhatsAppImageMessage(BaseModel):
    id: str
    name: str
    image_base64: str
    image_json: dict
    sender_phone_number: str