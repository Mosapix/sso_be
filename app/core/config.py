from os import getenv

from pydantic_settings import BaseSettings, SettingsConfigDict
from dotenv import load_dotenv

load_dotenv()

class Settings(BaseSettings):
    model_config = SettingsConfigDict(extra='allow', env_file='.env')

    app_name: str = getenv("APP_NAME")
    database_url: str = f"{getenv('DB_ENGINE')}://{getenv('DB_USER')}:{getenv('DB_PASSWORD')}@{getenv('DB_HOST')}:{getenv('DB_PORT')}/{getenv('DB_NAME')}"
    secret_key: str = getenv('SECRET_KEY')
    algorithm: str = getenv('ALGORITHM')
    access_token_expire_minutes: int = int(getenv('ACCESS_TOKEN_EXPIRE_MINUTES'))

settings = Settings()