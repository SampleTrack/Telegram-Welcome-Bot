import logging
import traceback
from datetime import datetime
from pyrogram.types import ChatMember
from pyrogram.enums import ChatMemberStatus


# ─────────────────────────────────────────
#  Logger Setup
# ─────────────────────────────────────────

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
    handlers=[
        logging.FileHandler("logs/bot.log"),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)


# ─────────────────────────────────────────
#  User Helpers (used in welcome + admin)
# ─────────────────────────────────────────

def mention(user) -> str:
    """Returns clickable markdown mention"""
    return f"[{user.first_name}](tg://user?id={user.id})"


def format_welcome(template: str, user, chat) -> str:
    """Format welcome message with placeholders"""
    return template.format(
        name=mention(user),
        first_name=user.first_name or "",
        last_name=user.last_name or "",
        username=f"@{user.username}" if user.username else user.first_name,
        group=chat.title,
        id=user.id,
        count=getattr(chat, "members_count", "")
    )


def is_admin(member: ChatMember) -> bool:
    """Check if member is admin or owner"""
    return member.status in [
        ChatMemberStatus.ADMINISTRATOR,
        ChatMemberStatus.OWNER
    ]


async def check_admin(client, message) -> bool:
    """Check if message sender is admin"""
    member = await client.get_chat_member(
        message.chat.id,
        message.from_user.id
    )
    return is_admin(member)


def now() -> str:
    """Returns formatted current datetime"""
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


# ─────────────────────────────────────────
#  Error Helper (used in all plugins)
# ─────────────────────────────────────────

def get_error_info(e: Exception) -> dict:
    """Extract error details for logging"""
    tb = traceback.extract_tb(e.__traceback__)
    last = tb[-1] if tb else None
    return {
        "error": str(e),
        "file": last.filename if last else "unknown",
        "line": last.lineno if last else "unknown"
    }


# ─────────────────────────────────────────
#  Log Channel Helper (used in all plugins)
# ─────────────────────────────────────────

async def send_log(client, log_channel_id: int, text: str):
    """Send message to log channel safely"""
    if not log_channel_id:
        return
    try:
        await client.send_message(log_channel_id, text)
    except Exception as e:
        logger.error(f"Log channel error: {e}")
