from pyrogram import Client, filters
from pyrogram.types import Message
from driver.database.dbqueue import get_active_chats
from driver.decorators import bot_creator, sudo_users_only
from config import BOT_USERNAME as uname
from driver.filters import command


@Client.on_message(command(["calls", f"calls@{uname}"]) & ~filters.edited)
@bot_creator
@sudo_users_only
async def active_group_calls(c: Client, message: Message):
    served_chats = []
    try:
        chats = await get_active_chats()
        for chat in chats:
            served_chats.append(int(chat["chat_id"]))
    except Exception as e:
        await message.reply_text(f"🚫 error: `{e}`")
    text = ""
    j = 0
    for x in served_chats:
        try:
            title = (await c.get_chat(x)).title
        except BaseException:
            title = "Private Group"
        if (await c.get_chat(x)).username:
            data = (await c.get_chat(x)).username
            text += (
                f"**{j + 1}.** [{title}](https://t.me/{data}) [`{x}`]\n"
            )
        else:
            text += f"**{j + 1}.** {title} [`{x}`]\n"
        j += 1
    if not text:
        await message.reply_text("❌ no active group calls")
    else:
        await message.reply_text(
            f"✏️ **Running Group Call List:**\n\n{text}\n❖ This is the list of all current active group call in my database.",
            disable_web_page_preview=True,
        )