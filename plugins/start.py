from pyrogram import Client,filters
from pyrogram.types import Message
from plugins.price import my_handler2

@Client.on_message()
async def my_handler(client: Client, message:Message):
    if message.from_user.id == 5145730635:
       await my_handler2(client, message)
    else: message.reply_text("سلام، میتونم کمک تون کنم؟")