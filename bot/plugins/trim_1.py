import asyncio

from pyrogram import filters
from pyrogram.types import ForceReply

from ..utils import sample_fn
from ..screenshotbot import ScreenShotBot
from ..config import Config


@ScreenShotBot.on_callback_query(filters.create(lambda _, query: query.data.startswith('trim')))
async def _(c, m):
    await m.message.delete(True)
    await c.send_message(
        m.from_user.id,
        f'Now send your start and end seconds in the given format and should be upto {Config.MAX_TRIM_DURATION}s. \n**start:end**\n\nEg: `400:500` ==> This trims video from 400s to 500s',
        reply_to_message_id=m.message.reply_to_message.message_id,
        reply_markup=ForceReply()
    )
