from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from database import set_welcome, set_rules, toggle_setting, get_setting
from utils import check_admin, send_log, logger, get_error_info
from strings import (
    ADMIN_ONLY, SETTINGS_MSG, WELCOME_UPDATED,
    WELCOME_RESET, RULES_UPDATED, DEFAULT_RULES,
    DEFAULT_WELCOME, INVALID_CMD, ERROR_LOG
)
from config import LOG_CHANNEL_ID
import os


def settings_keyboard(
    welcome_on: bool,
    ban_bots: bool,
    clean_joins: bool,
    rules_button: bool
) -> InlineKeyboardMarkup:
    def toggle(val): return "✅ ON" if val else "❌ OFF"
    return InlineKeyboardMarkup([
        [
            InlineKeyboardButton("👋 Welcome Msg", callback_data="noop"),
            InlineKeyboardButton(toggle(welcome_on), callback_data="toggle_welcome")
        ],
        [
            InlineKeyboardButton("🤖 Ban Bots", callback_data="noop"),
            InlineKeyboardButton(toggle(ban_bots), callback_data="toggle_banbots")
        ],
        [
            InlineKeyboardButton("🧹 Clean Joins", callback_data="noop"),
            InlineKeyboardButton(toggle(clean_joins), callback_data="toggle_cleanjoins")
        ],
        [
            InlineKeyboardButton("📜 Rules Button", callback_data="noop"),
            InlineKeyboardButton(toggle(rules_button), callback_data="toggle_rules_btn")
        ]
    ])


@Client.on_message(filters.command("settings") & filters.group)
async def settings(client: Client, message: Message):
    if not await check_admin(client, message):
        return await message.reply(ADMIN_ONLY)
    chat_id = message.chat.id
    keyboard = settings_keyboard(
        welcome_on=await get_setting(chat_id, "welcome_enabled", True),
        ban_bots=await get_setting(chat_id, "ban_bots", True),
        clean_joins=await get_setting(chat_id, "clean_joins", True),
        rules_button=await get_setting(chat_id, "rules_button", True)
    )
    await message.reply(SETTINGS_MSG, reply_markup=keyboard)


@Client.on_message(filters.command("setwelcome") & filters.group)
async def setwelcome(client: Client, message: Message):
    if not await check_admin(client, message):
        return await message.reply(ADMIN_ONLY)
    if len(message.command) < 2:
        return await message.reply(
            INVALID_CMD.format(
                usage="/setwelcome Your message\n\n"
                "**Placeholders:**\n"
                "`{name}` — mention\n"
                "`{first_name}` — first name\n"
                "`{group}` — group name\n"
                "`{count}` — member count"
            )
        )
    text = message.text.split(None, 1)[1]
    await set_welcome(message.chat.id, text)
    await message.reply(WELCOME_UPDATED)


@Client.on_message(filters.command("resetwelcome") & filters.group)
async def resetwelcome(client: Client, message: Message):
    if not await check_admin(client, message):
        return await message.reply(ADMIN_ONLY)
    await set_welcome(message.chat.id, DEFAULT_WELCOME)
    await message.reply(WELCOME_RESET)


@Client.on_message(filters.command("setrules") & filters.group)
async def setrules(client: Client, message: Message):
    if not await check_admin(client, message):
        return await message.reply(ADMIN_ONLY)
    if len(message.command) < 2:
        return await message.reply(
            INVALID_CMD.format(usage="/setrules Your rules here")
        )
    text = message.text.split(None, 1)[1]
    await set_rules(message.chat.id, text)
    await message.reply(RULES_UPDATED)


@Client.on_message(filters.command("logs") & filters.private)
async def logs(client: Client, message: Message):
    try:
        if not os.path.exists("logs/bot.log"):
            return await message.reply("📭 No logs found yet!")
        await message.reply_document(
            "logs/bot.log",
            caption="📋 **Bot Error Logs**"
        )
    except Exception as e:
        await message.reply("⚠️ Could not fetch logs!")
        logger.error(f"Logs command error: {e}")


# ─── Toggle Callbacks ───────────────────────────────

async def refresh_settings(callback_query, client):
    """Refresh settings keyboard after toggle"""
    chat_id = callback_query.message.chat.id
    keyboard = settings_keyboard(
        welcome_on=await get_setting(chat_id, "welcome_enabled", True),
        ban_bots=await get_setting(chat_id, "ban_bots", True),
        clean_joins=await get_setting(chat_id, "clean_joins", True),
        rules_button=await get_setting(chat_id, "rules_button", True)
    )
    await callback_query.message.edit_reply_markup(keyboard)


@Client.on_callback_query(filters.regex("toggle_welcome"))
async def toggle_welcome(client, callback_query):
    chat_id = callback_query.message.chat.id
    current = await get_setting(chat_id, "welcome_enabled", True)
    await toggle_setting(chat_id, "welcome_enabled", not current)
    status = "✅ ON" if not current else "❌ OFF"
    await callback_query.answer(f"👋 Welcome Message {status}", show_alert=True)
    await refresh_settings(callback_query, client)


@Client.on_callback_query(filters.regex("toggle_banbots"))
async def toggle_banbots(client, callback_query):
    chat_id = callback_query.message.chat.id
    current = await get_setting(chat_id, "ban_bots", True)
    await toggle_setting(chat_id, "ban_bots", not current)
    status = "✅ ON" if not current else "❌ OFF"
    await callback_query.answer(f"🤖 Ban Bots {status}", show_alert=True)
    await refresh_settings(callback_query, client)


@Client.on_callback_query(filters.regex("toggle_cleanjoins"))
async def toggle_cleanjoins(client, callback_query):
    chat_id = callback_query.message.chat.id
    current = await get_setting(chat_id, "clean_joins", True)
    await toggle_setting(chat_id, "clean_joins", not current)
    status = "✅ ON" if not current else "❌ OFF"
    await callback_query.answer(f"🧹 Clean Joins {status}", show_alert=True)
    await refresh_settings(callback_query, client)


@Client.on_callback_query(filters.regex("toggle_rules_btn"))
async def toggle_rules_btn(client, callback_query):
    chat_id = callback_query.message.chat.id
    current = await get_setting(chat_id, "rules_button", True)
    await toggle_setting(chat_id, "rules_button", not current)
    status = "✅ ON" if not current else "❌ OFF"
    await callback_query.answer(f"📜 Rules Button {status}", show_alert=True)
    await refresh_settings(callback_query, client)


@Client.on_callback_query(filters.regex("noop"))
async def noop(client, callback_query):
    await callback_query.answer("👆 Use the button next to this!", show_alert=True)
