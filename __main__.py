from pyrogram import Client
import pyromod.listen

plugins = dict(root="plugins")

app = Client(name="my_self_bot",
             api_id=29470616,
             api_hash="01d00f7492d0672c7276e76d9c737b41",
             plugins=plugins)

app.run()