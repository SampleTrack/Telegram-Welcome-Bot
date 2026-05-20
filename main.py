import os
import asyncio
from pyrogram import Client
from pyrogram.errors import FloodWait

from config import API_ID, API_HASH, BOT_TOKEN, LOG_CHANNEL_ID, BOT_NAME
from utils import logger, send_log, now
from strings import BOT_STARTED
import plugins

# Create logs directory if not exists
os.makedirs("logs", exist_ok=True)

app = Client(
    "welcome_bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)


async def run():
    await app.start()
    me = await app.get_me()
    logger.info(f"Bot started: @{me.username}")
    await send_log(
        app, LOG_CHANNEL_ID,
        BOT_STARTED.format(
            bot_name=BOT_NAME,
            time=now()
        )
    )
    await asyncio.get_event_loop().create_future()  # Run forever


if __name__ == "__main__":
    logger.info("Starting bot...")
    app.run(run())
