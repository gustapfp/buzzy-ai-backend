from src.agents.state_classifier.client import StateClassifierAgent
from src.agents.state_classifier.schemas import MessageClassification
from src.integrations.evolutionApi.schemas import WhatsAppTextMessage
from src.config.config import settings
from src.integrations.n8n_integration.router import send_message_to_agent
from structlog import get_logger

class IntegrationHandler:
    def __init__(self):
        self.agents_urls = settings.agents_urls
        self.classifier_agent = StateClassifierAgent()
        self.logger = get_logger()
        
    async def send_to_agent(self, message: WhatsAppTextMessage) -> None:
        """This methods receive a WhatsApp text message and send it to the appropriate agent.

        Args:
            message (WhatsAppTextMessage): WhatsApp text message received from Evolution API.

        Returns:
            None: None
        """
        classification = self.classifier_agent.classify_text_message(message.text)
        agent_url = self.__get_agent_url(classification)
        if agent_url:
            self.logger.info(f"Sending message to agent: {agent_url}")
            self.logger.info(f"Classification: {classification}")
            await send_message_to_agent(
                classification=classification, 
                whatsapp_message=message, 
                url=agent_url)
        else:
            self.logger.error(f"No agent url found for classification: {classification}")
        return None

    def __get_agent_url(self, message: MessageClassification) -> str:
        return self.agents_urls.get(message.category.value)
