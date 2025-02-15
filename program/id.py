
from pyrogram import Client, filters
from pyrogram.types import Message

from config import BOT_USERNAME, SUDO_USERS
from driver.filters import command, eor
from driver.core import bot as c, user as nikki

def get_file_id(msg: Message):
    if msg.media:
        for message_type in (
            "photo",
            "animation",
            "audio",
            "document",
            "video",
            "video_note",
            "voice",
            # "contact",
            # "dice",
            # "poll",
            # "location",
            # "venue",
            "sticker",
        ):
            obj = getattr(msg, message_type)
            if obj:
                setattr(obj, "message_type", message_type)
                return obj    
"""
Get id of the replied user
Syntax: /id
"""


@Client.on_message(command(["id", f"id@{BOT_USERNAME}"]))
async def showid(_, message: Message):
    chat_type = message.chat.type

    if chat_type == "private":
        user_id = message.chat.id
        await message.reply_text(f"<code>{user_id}</code>")

    elif chat_type in ["group", "supergroup"]:
        _id = ""
        _id += "<b>Chat ID</b>: " f"<code>{message.chat.id}</code>\n"
        if message.reply_to_message:
            _id += (
                "<b>Replied User ID</b>: "
                f"<code>{message.reply_to_message.from_user.id}</code>\n"
            )
            file_info = get_file_id(message.reply_to_message)
        else:
            _id += "<b>User ID</b>: " f"<code>{message.from_user.id}</code>\n"
            file_info = get_file_id(message)
        if file_info:
            _id += (
                f"<b>{file_info.message_type}</b>: "
                f"<code>{file_info.file_id}</code>\n"
            )
        await message.reply_text(_id)

@nikki.on_message(filters.command("id", [".", "!","#"]) & filters.user(SUDO_USERS) & ~filters.edited)
async def showid(_, message: Message):
    chat_type = message.chat.type

    if chat_type == "private":
        user_id = message.chat.id
        await eor(message,f"<code>{user_id}</code>")

    elif chat_type in ["group", "supergroup"]:
        _id = ""
        _id += "<b>Chat ID</b>: " f"<code>{message.chat.id}</code>\n"
        if message.reply_to_message:
            _id += (
                "<b>Replied User ID</b>: "
                f"<code>{message.reply_to_message.from_user.id}</code>\n"
            )
            file_info = get_file_id(message.reply_to_message)
        else:
            _id += "<b>User ID</b>: " f"<code>{message.from_user.id}</code>\n"
            file_info = get_file_id(message)
        if file_info:
            _id += (
                f"<b>{file_info.message_type}</b>: "
                f"<code>{file_info.file_id}</code>\n"
            )
        await eor(message,_id)