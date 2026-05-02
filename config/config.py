import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    BASE_URL = os.getenv("BASE_URL")
    TIMEOUT  = int(os.getenv("TIMEOUT", "10"))
    API_KEY  = os.getenv("API_KEY")

