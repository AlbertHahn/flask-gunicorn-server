from pydantic import BaseSettings
import os

class AppSettings(BaseSettings):
    url: str = os.getenv("URL")