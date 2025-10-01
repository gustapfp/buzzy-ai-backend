from pydantic import BaseModel

class WhatsAppMessageSchema(BaseModel):
    message:str
    recipient_phone_number: str
