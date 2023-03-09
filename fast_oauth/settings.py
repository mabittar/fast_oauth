from dotenv import find_dotenv
from pydantic import BaseSettings, Field


class EnvSettings(BaseSettings):
    github_client_id: str = Field(default="", env="GITHUB_CLIENT_ID")
    github_client_secret: str = Field(default="", env="GITHUB_CLIENT_SECRET")

    class Config:
        env_file = find_dotenv(filename=".env", usecwd=True)
        env_file_encoding = "utf-8"


settings = EnvSettings()
