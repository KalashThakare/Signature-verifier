from pydantic_settings import BaseSettings
from functools import lru_cache
from pydantic import Field, ConfigDict

class Settings(BaseSettings):
    PORT: int = Field(8000, env="PORT")
    ALLOWED_ORIGINS: list[str] = ["http://localhost:3000"]
    model_config = ConfigDict(
        extra="ignore",  
        env_file=".env",   
    )

@lru_cache
def get_settings() -> Settings:
    return Settings()

settings = get_settings()
