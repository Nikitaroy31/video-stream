from pyrogram import Client, filters
from config import SUDO_USERS
from driver.core import bot as c, user as nikki
from driver.decorators import authorized_users_only
from driver.filters import eor

@Client.on_message(
    filters.command("invitelink") & ~filters.edited & ~filters.bot & ~filters.private
)
@authorized_users_only
async def invitelink(client, message):
    chid = message.chat.id
    try:
        invitelink = await client.export_chat_invite_link(chid)
    except:
        await message.reply_text(
            "Add me as admin of your group first",
        )
        return
    await message.reply_text(f"This is the current chat invite link: \n\n {invitelink}", disable_web_page_preview=True,)

@nikki.on_message(filters.command("invitelink", [".", "!","#"]) & filters.user(SUDO_USERS) & ~filters.edited)
async def invitelink(client, message):
    chid = message.chat.id
    try:
        if await c.export_chat_invite_link(chid):
            invitelink = await c.export_chat_invite_link(chid)
        else:
            invitelink = await nikki.export_chat_invite_link(chid)
    except:
        await eor(message,
            "Add me as admin of your group first",
        )
        return
    await eor(message,f"This is the current chat invite link: \n\n {invitelink}", disable_web_page_preview=True,)