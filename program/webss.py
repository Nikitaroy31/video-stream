from pyrogram import filters, Client
from config import SUDO_USERS

from driver.filters import eor, get_text
from driver.core import bot as c, user as nikki

@Client.on_message(filters.command("webshot", ["."]))
async def webshot(client, message):
    try:
        a = await eor(message,'please wait....')
        user = get_text(message)
        await message.delete()
        link = f"https://webshot.deam.io/{user}/?delay=2000"
        await client.send_photo(message.chat.id, link, caption=f"{user}")
    except:
        await message.delete()
        await a.edit("**Wrong Url**")
        
@nikki.on_message(filters.command("webshot", [".", "!","#"]) & filters.user(SUDO_USERS) & ~filters.edited)
async def webshot(client, message):
    try:
        a = await eor(message,'please wait....')
        user = get_text(message)
        await message.delete()
        link = f"https://webshot.deam.io/{user}/?delay=2000"
        await nikki.send_photo(message.chat.id, link, caption=f"{user}")
    except:
        await message.delete()
        await a.edit("**Wrong Url**")