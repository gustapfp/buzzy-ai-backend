class WhatsAppMessageTransformer:
    def number_link_to_phone_number(self, number_link: str) -> str:
        """
        Extracts the phone number from a WhatsApp number link.
        E.g. '554896604747@s.whatsapp.net' -> '554896604747'
        """
        return number_link.split("@")[0] if "@" in number_link else number_link