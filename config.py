import os
from dotenv import load_dotenv

load_dotenv()

# Telegram
API_ID = int(os.getenv("API_ID", 0))
API_HASH = os.getenv("API_HASH", "")
BOT_TOKEN = os.getenv("BOT_TOKEN", "")

# MongoDB
MONGO_URI = os.getenv("MONGO_URI", "")
DB_NAME = os.getenv("DB_NAME", "welcome_bot")

# Bot Settings
LOG_CHANNEL_ID = int(os.getenv("LOG_CHANNEL_ID", 0))
SUPPORT_LINK = os.getenv("SUPPORT_LINK", "")
BOT_NAME = os.getenv("BOT_NAME", "Welcome Bot")
