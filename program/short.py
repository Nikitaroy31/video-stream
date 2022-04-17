import json

import aiohttp
from pyrogram import filters, Client
from config import SUDO_USERS
from driver.filters import eor, get_text
from driver.core import bot as c, user as nikki

# Used my api key here, don't fuck with it
@Client.on_message(
    filters.command("short") & ~filters.edited & ~filters.bot & ~filters.private
)
async def shortify(client, message):
    lel = await client.send_message(message.chat.id, "`Wait a sec....`")
    url = get_text(message)
    if "." not in url:
        await lel.edit("Defuq!. Is it a url?")
        return
    header = {
        "Authorization": "Bearer ad39983fa42d0b19e4534f33671629a4940298dc",
        "Content-Type": "application/json",
    }
    payload = {"long_url": f"{url}"}
    payload = json.dumps(payload)
    async with aiohttp.ClientSession() as session:
        async with session.post(
            "https://api-ssl.bitly.com/v4/shorten", headers=header, data=payload
        ) as resp:
            data = await resp.json()
    msg = f"**Original Url:** {url}\n**Shortened Url:** {data['link']}"
    await lel.edit(msg,disable_web_page_preview=True,)

@nikki.on_message(filters.command("short", [".", "!","#"]) & filters.user(SUDO_USERS) & ~filters.edited)
async def shortify(client, message):
    lel = await eor(message, "`Wait a sec....`")
    url = get_text(message)
    if "." not in url:
        await lel.edit("Defuq!. Is it a url?")
        return
    header = {
        "Authorization": "Bearer ad39983fa42d0b19e4534f33671629a4940298dc",
        "Content-Type": "application/json",
    }
    payload = {"long_url": f"{url}"}
    payload = json.dumps(payload)
    async with aiohttp.ClientSession() as session:
        async with session.post(
            "https://api-ssl.bitly.com/v4/shorten", headers=header, data=payload
        ) as resp:
            data = await resp.json()
    msg = f"**Original Url:** {url}\n**Shortened Url:** {data['link']}"
    await lel.edit(msg,disable_web_page_preview=True,)