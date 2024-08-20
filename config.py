from pydantic import (
    Field,
    AnyUrl,
)
import httpx
from pydantic_settings import BaseSettings, SettingsConfigDict




class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file='.env', env_file_encoding='utf-8')

    api_key: str = Field(alias='api_key')
    api_url: str = Field(alias='api_url')


