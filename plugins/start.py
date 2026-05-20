from pyrogram import Client, filters
from pyrogram.types import Message
from strings import START_MSG
from config import BOT_NAME


@Client.on_message(filters.command("start") & filters.private)
async def start(client: Client, message: Message):
    await message.reply(
        START_MSG.format(bot_name=BOT_NAME),
        disable_web_page_preview=True
    )
