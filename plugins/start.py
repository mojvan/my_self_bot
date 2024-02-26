from pyrogram import Client,filters
from pyrogram.types import Message

@Client.on_message(filters.regex("سلام"))
async def my_handler(client: Client, message:Message):
    await message.reply_text("سلام، میتونم کمک تون کنم؟")