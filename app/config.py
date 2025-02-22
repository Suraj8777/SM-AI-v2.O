import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    OPENWEATHER_API_KEY = os.getenv("OPENWEATHER_API_KEY")
    SCENE_API_KEY = os.getenv("SCENE_API_KEY")
    OPENAI_API_KEYS = os.getenv("OPENAI_API_KEYS").split(",")
