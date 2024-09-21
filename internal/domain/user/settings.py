from dotenv import load_dotenv, find_dotenv
from pydantic_settings import BaseSettings

load_dotenv(find_dotenv(".env"))


class Settings(BaseSettings):
    # Authentication settings
    token_secret_key: str
    token_algorithm: str


def get_settings():
    # TODO: create different settings based on environment (production, testing, etc.)
    return Settings()
