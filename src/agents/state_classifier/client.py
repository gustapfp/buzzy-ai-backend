from src.agents.state_classifier.types import MessageClassification
from src.config.config import settings
import instructor
from src.agents.state_classifier.prompt import STATE_CLASSIFIER_PROMPT
from openai import OpenAI

class StateClassifierAgent:
    def __init__(self):
        self.client = instructor.from_openai(OpenAI(api_key=settings.openai_api_key))
        self.openai_model = "gpt-4o-mini"
        self.instructions = STATE_CLASSIFIER_PROMPT
        self.max_retries = 3
    # TODO: Define messages format
    def classify_message(self, message: str) -> MessageClassification:
        response = self.client.chat.completions.create(
            model=self.openai_model,
            response_model=MessageClassification,
            temperature=0.0,
            max_retries=self.max_retries,
            messages={

                {
                    "role": "system",
                    "content": self.instructions,
                },
                {
                    "role": "user",
                    "content": message,
                },
            },
        )
        return response