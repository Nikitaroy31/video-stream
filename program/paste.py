import os

import requests
from pyrogram import filters, Client
from config import SUDO_USERS
from driver.filters import eor, get_text
from driver.core import bot as c, user as nikki

@Client.on_message(filters.command("paste") & ~filters.edited & ~filters.bot)
async def paste(client, message):
    pablo = await eor(message, "`Please Wait.....`")
    tex_t = get_text(message)
    message_s = tex_t
    if not tex_t:
        if not message.reply_to_message:
            await pablo.edit("`Reply To File / Give Me Text To Paste!`")
            return
        if not message.reply_to_message.text:
            file = await message.reply_to_message.download()
            m_list = open(file, "r").read()
            message_s = m_list
            print(message_s)
            os.remove(file)
        elif message.reply_to_message.text:
            message_s = message.reply_to_message.text
    key = (
        requests.post("https://nekobin.com/api/documents", json={"content": message_s})
        .json()
        .get("result")
        .get("key")
    )
    url = f"https://nekobin.com/{key}"
    raw = f"https://nekobin.com/raw/{key}"
    reply_text = f"Pasted Text To [NekoBin]({url}) And For Raw [Click Here]({raw})"
    await pablo.edit(reply_text,disable_web_page_preview=True)
    link = f"https://webshot.deam.io/{url}/?delay=2000"
    await message.reply_photo(link, caption=f"Screenshort")

@nikki.on_message(filters.command("paste", [".", "!","#"]) & filters.user(SUDO_USERS) & ~filters.edited)
async def paste(client, message):
    pablo = await eor(message, "`Please Wait.....`")
    tex_t = get_text(message)
    message_s = tex_t
    if not tex_t:
        if not message.reply_to_message:
            await pablo.edit("`Reply To File / Give Me Text To Paste!`")
            return
        if not message.reply_to_message.text:
            file = await message.reply_to_message.download()
            m_list = open(file, "r").read()
            message_s = m_list
            print(message_s)
            os.remove(file)
        elif message.reply_to_message.text:
            message_s = message.reply_to_message.text
    key = (
        requests.post("https://nekobin.com/api/documents", json={"content": message_s})
        .json()
        .get("result")
        .get("key")
    )
    url = f"https://nekobin.com/{key}"
    raw = f"https://nekobin.com/raw/{key}"
    reply_text = f"Pasted Text To [NekoBin]({url}) And For Raw [Click Here]({raw})"
    await pablo.edit(reply_text,disable_web_page_preview=True)
    link = f"https://webshot.deam.io/{url}/?delay=2000"
    await message.reply_photo(link, caption=f"Screenshort")