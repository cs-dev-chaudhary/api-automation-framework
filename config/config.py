import os
from dotenv import load_dotenv

def load_env(env_name=None):
    if env_name:
        load_dotenv(f".env.{env_name}", override=True)
    else:
        load_dotenv()
    Config.reload()

class Config:
    BASE_URL = None
    TIMEOUT  = 10
    API_KEY  = None

    @classmethod
    def reload(cls):
        cls.BASE_URL = os.getenv("BASE_URL")
        cls.TIMEOUT  = int(os.getenv("TIMEOUT", "10"))
        cls.API_KEY  = os.getenv("API_KEY")
