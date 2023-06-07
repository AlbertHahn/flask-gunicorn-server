from pydantic import BaseSettings
import os

class AppSettings(BaseSettings):
    content: str = os.getenv("CONTENT")

appSettings = AppSettings() 