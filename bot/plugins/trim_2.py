import asyncio

from pyrogram import filters, ForceReply

from ..config import Config
from ..utils import trim_fn
from ..screenshotbot import ScreenShotBot


@ScreenShotBot.on_message(filters.private & filters.reply)
async def _(c, m):
    
    if not await c.db.is_user_exist(m.chat.id):
        await c.db.add_user(m.chat.id)
        await c.send_message(
            Config.LOG_CHANNEL,
            f"New User [{m.from_user.first_name}](tg://user?id={m.chat.id}) started."
        )
    
    if not m.reply_to_message.reply_markup:
        print('no reply_markup')
        return
    
    if not isinstance(m.reply_to_message.reply_markup, ForceReply):
        print('not ForceReply')
        return
    
    asyncio.create_task(trim_fn(c, m))
