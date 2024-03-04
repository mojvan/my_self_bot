from pyrogram import Client,filters
from pyrogram.types import Message
from pycoingecko import CoinGeckoAPI
cg = CoinGeckoAPI()

@Client.on_message(filters.regex("قیمت"))
async def my_handler(client: Client, message:Message):
    # price =  cg.get_price(ids='bitcoin', vs_currencies='usd')
    # await message.reply_text(f"{price["bitcoin"]["usd"]}")
    #
    #
    # await client.join_chat("hamamsssss")
    chat = await client.get_chat("hamamsssss")
    print(chat.id)
    await client.send_message(chat_id=int(chat.id),text="hello")
    # print(chat.id)