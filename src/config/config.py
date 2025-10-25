from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    openai_api_key: str
    agents_urls: dict[str, str]

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()
