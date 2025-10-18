from enum import Enum

from pydantic import BaseModel, Field


class MessageCategory(str, Enum):
    CURIOUS = "curioso"
    INTERESTED = "interessado"
    BUYER = "comprador"
    NO_RESPONSE = "sem_resposta"
    NO_INTEREST = "sem_interesse"
    GREETING = "saudacao"

class ClientSentiment(str, Enum):
    ANGRY = "irritado"
    FRUSTRATED = "frustrado"
    NEUTRAL = "neutro"

class MessageUrgency(str, Enum):
    LOW = "baixa"
    MEDIUM = "media"
    HIGH = "alta"

class MessageClassification(BaseModel):
    category: MessageCategory
    sentiment: ClientSentiment
    urgency: MessageUrgency
    confidence: float = Field(ge=0, le=1, description="Confidence in the classification")
    key_information: str = Field(description="Key information from the message that helps to classify it")
    suggested_actions: list[str] = Field(description="Suggested actions to take based on the classification")