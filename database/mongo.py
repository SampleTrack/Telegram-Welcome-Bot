import motor.motor_asyncio
from config import MONGO_URI, DB_NAME

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_URI)
db = client[DB_NAME]
groups_col = db["groups"]


async def get_group(chat_id: int) -> dict:
    return await groups_col.find_one({"chat_id": chat_id})


async def update_group(chat_id: int, data: dict):
    await groups_col.update_one(
        {"chat_id": chat_id},
        {"$set": data},
        upsert=True
    )


async def get_welcome(chat_id: int) -> str | None:
    group = await get_group(chat_id)
    return group.get("welcome_message") if group else None


async def get_rules(chat_id: int) -> str | None:
    group = await get_group(chat_id)
    return group.get("rules") if group else None


async def set_welcome(chat_id: int, message: str):
    await update_group(chat_id, {"welcome_message": message})


async def set_rules(chat_id: int, rules: str):
    await update_group(chat_id, {"rules": rules})


async def toggle_setting(chat_id: int, key: str, value: bool):
    await update_group(chat_id, {key: value})


async def get_setting(chat_id: int, key: str, default=True) -> bool:
    group = await get_group(chat_id)
    return group.get(key, default) if group else default
