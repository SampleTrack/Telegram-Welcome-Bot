from pyrogram import Client, filters
from pyrogram.types import ChatMemberUpdated, InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.enums import ChatMemberStatus

from database import get_welcome, get_rules, get_setting
from utils import mention, format_welcome, send_log, logger, get_error_info
from strings import DEFAULT_WELCOME, NEW_MEMBER_LOG, BOT_BANNED_LOG, ERROR_LOG
from config import LOG_CHANNEL_ID


@Client.on_chat_member_updated()
async def welcome(client: Client, update: ChatMemberUpdated):
    try:
        # Only new members joining
        if not (
            update.new_chat_member and
            update.new_chat_member.status == ChatMemberStatus.MEMBER and
            (update.old_chat_member is None or
             update.old_chat_member.status in [
                 ChatMemberStatus.LEFT,
                 ChatMemberStatus.BANNED
             ])
        ):
            return

        chat = update.chat
        user = update.new_chat_member.user

        # Auto ban bots
        if await get_setting(chat.id, "ban_bots", True) and user.is_bot:
            await client.ban_chat_member(chat.id, user.id)
            await send_log(
                client, LOG_CHANNEL_ID,
                BOT_BANNED_LOG.format(
                    name=user.first_name,
                    user_id=user.id,
                    group=chat.title
                )
            )
            return

        # Check welcome enabled
        if not await get_setting(chat.id, "welcome_enabled", True):
            return

        # Format welcome message
        template = await get_welcome(chat.id) or DEFAULT_WELCOME
        text = format_welcome(template, user, chat)

        # Build keyboard
        buttons = []
        if await get_setting(chat.id, "rules_button", True):
            buttons.append([
                InlineKeyboardButton("📜 Read Rules", callback_data="show_rules")
            ])
        keyboard = InlineKeyboardMarkup(buttons) if buttons else None

        # Send welcome
        await client.send_message(
            chat_id=chat.id,
            text=text,
            reply_markup=keyboard,
            disable_web_page_preview=True
        )

        # Log new member
        await send_log(
            client, LOG_CHANNEL_ID,
            NEW_MEMBER_LOG.format(
                name=mention(user),
                user_id=user.id,
                group=chat.title,
                chat_id=chat.id
            )
        )

    except Exception as e:
        info = get_error_info(e)
        logger.error(f"Welcome error: {info}")
        await send_log(
            client, LOG_CHANNEL_ID,
            ERROR_LOG.format(**info)
        )


@Client.on_callback_query(filters.regex("show_rules"))
async def show_rules(client, callback_query):
    try:
        rules = await get_rules(callback_query.message.chat.id)
        await callback_query.answer(
            rules[:200] if rules else "⚠️ No rules set yet!",
            show_alert=True
        )
    except Exception as e:
        await callback_query.answer("⚠️ Error fetching rules!", show_alert=True)
        logger.error(f"Rules callback error: {e}")
