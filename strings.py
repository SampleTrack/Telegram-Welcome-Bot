
# ─────────────────────────────────────────
#  All reusable text strings for the bot
# ─────────────────────────────────────────

# Bot Messages
START_MSG = (
    "👋 **Welcome to {bot_name}!**\n\n"
    "I help you manage your Telegram groups professionally.\n\n"
    "**✨ Features:**\n"
    "• Auto welcome new members\n"
    "• Custom welcome messages\n"
    "• Group rules management\n"
    "• Auto ban spam bots\n"
    "• Clean join/leave messages\n\n"
    "**📌 How to use:**\n"
    "1. Add me to your group\n"
    "2. Make me an Admin\n"
    "3. Use /settings to configure\n\n"
    "**⚡ Commands:**\n"
    "/setwelcome — Set welcome message\n"
    "/resetwelcome — Reset to default\n"
    "/setrules — Set group rules\n"
    "/settings — Bot settings panel\n"
    "/logs — View recent error logs"
)

# Welcome
DEFAULT_WELCOME = (
    "👋 Welcome {name} to **{group}**!\n\n"
    "We're glad to have you here. 😊\n"
    "Please read the rules before chatting!"
)

# Rules
DEFAULT_RULES = (
    "📜 **Group Rules:**\n\n"
    "1. Be respectful to everyone\n"
    "2. No spam or advertisements\n"
    "3. No NSFW content\n"
    "4. Follow admin instructions\n\n"
    "⚠️ Violation = Ban!"
)

# Admin Only
ADMIN_ONLY = "❌ This command is for **admins only!**"

# Errors
ERROR_MSG = "⚠️ Something went wrong. Please try again!"
INVALID_CMD = "❌ Invalid usage!\n\n{usage}"

# Settings
SETTINGS_MSG = (
    "⚙️ **Group Settings**\n\n"
    "Toggle features using the buttons below:"
)

# Logs
BOT_STARTED = (
    "🟢 **{bot_name} Started!**\n\n"
    "🕐 Time: {time}\n"
    "📦 Version: 1.0.0"
)

NEW_MEMBER_LOG = (
    "👤 **New Member Joined**\n\n"
    "• Name: {name}\n"
    "• ID: `{user_id}`\n"
    "• Group: {group}\n"
    "• Group ID: `{chat_id}`"
)

BOT_BANNED_LOG = (
    "🤖 **Bot Banned**\n\n"
    "• Bot: {name}\n"
    "• ID: `{user_id}`\n"
    "• Group: {group}"
)

ERROR_LOG = (
    "🔴 **Error Occurred**\n\n"
    "• Error: `{error}`\n"
    "• File: `{file}`\n"
    "• Line: `{line}`"
)

WELCOME_UPDATED = "✅ Welcome message updated successfully!"
WELCOME_RESET = "✅ Welcome message reset to default!"
RULES_UPDATED = "✅ Rules updated successfully!"
