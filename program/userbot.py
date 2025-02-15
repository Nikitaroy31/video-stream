from config import BOT_USERNAME, OWNER_ID, SUDO_USERS, UPDATES_CHANNEL
from driver.core import user as nikki
from driver.core import me_user
from pyrogram import filters
from pyrogram.types import Dialog, Chat, Message
from time import time
from datetime import datetime
from pyrogram import Client, filters, __version__ as pyrover
from pytgcalls import (__version__ as pytgver)
from driver.filters import eor, get_text
import requests
from program import __version__ as ver
from program.start import __python_version__ as pyver

import os



# To Block a PM'ed User
@nikki.on_message(filters.command("block", [".", "!","#"]) & filters.user(SUDO_USERS) & ~filters.edited)
async def ubblock(_, message: Message):
  shit_id = message.chat.id
  gonna_block_u = await eor(message,"`Blocking User...`")
  try:
    await nikki.block_user(shit_id)
    await gonna_block_u.edit("`Successfully Blocked This User`")
  except Exception as lol:
    await gonna_block_u.edit(f"`Can't Block This Guy! May be this is durov?` \n\n**Error:** `{lol}`")


# To Unblock User That Already Blocked
@nikki.on_message(filters.command("unblock", [".", "!","#"]) & filters.user(SUDO_USERS) & ~filters.edited)
async def ubblock(_, message: Message):
  good_bro = int(message.command[1])
  gonna_unblock_u = await eor(message,"`Unblocking User...`")
  try:
    await nikki.unblock_user(good_bro)
    await gonna_unblock_u.edit(f"`Successfully Unblocked The User` \n**User ID:** `{good_bro}`")
  except Exception as lol:
    await gonna_unblock_u.edit(f"`Can't Unblock That Guy!, I think he is still dumb!` \n\n**Error:** `{lol}`")


# To Get How Many Chats that you are in (PM's also counted)
@nikki.on_message(filters.private & filters.command("chats", [".", "!","#"]) & filters.user(SUDO_USERS) & ~filters.edited)
async def ubgetchats(_, message: Message):
  getting_chats = await eor(message,"`Checking Your Chats, Hang On...`")
  async for dialog in nikki.iter_dialogs():
    try:
      total = await nikki.get_dialogs_count()
      await getting_chats.edit(f"**Total Dialogs Counted:** `{total}` \n\n**Not Stable Lol**")
    except Exception as lol:
      brokenmsg = await eor(message, f"`Never Gonna Give You Up!, but Something Went Wrong!`")
      await brokenmsg.edit(f"**Error:** `{lol}`")


# Leave From a Chat
@nikki.on_message(filters.command("kickme", [".", "!","#"]) & filters.user(SUDO_USERS) & ~filters.edited)
async def ubkickme(_, message: Message):
  i_go_away = await eor(message,"`Leaving This Chat...`")
  try:
    await nikki.leave_chat(message.chat.id)
    await i_go_away.edit("`Successfully Leaved This Chat!`")
  except Exception as lol:
    await i_go_away.edit(f"`Can't Leave This Chat!, What a cruel world!` \n\n**Error:** `{lol}`")

PM_LOG = 'on'

@nikki.on_message(filters.private)
async def sendpmlol(client: nikki, message: Message):
  nikki_ID = int((await nikki.get_me()).id)
  if message.from_user.id == OWNER_ID or message.from_user.id == nikki_ID:
    return
  pmlogchat = -1001674515262
  userinfo = await client.get_users(user_ids=message.from_user.id)
  nibba = int(message.chat.id)
  msg_txt = message.text
  if PM_LOG == 'off':
    return
  else:
    try:
      forwardedmsg = await client.forward_messages(chat_id=pmlogchat, from_chat_id=message.chat.id, message_ids=message.message_id)
      await forwardedmsg.reply_text(f"**Incoming Message** \n\n**👤 User Info \n ⤷**User Name:** `{userinfo.first_name}` \n ⤷**Username:** @{userinfo.username} \n ⤷**User ID:** `{nibba}`", parse_mode="md")
    except Exception as lol:
      await client.send_message(chat_id=pmlogchat, text=f"`Something Wrong Happend While Sending Message!` \n\n**Error:** {lol}", parse_mode="md")



################ping###################

START_TIME = datetime.utcnow()
START_TIME_ISO = START_TIME.replace(microsecond=0).isoformat()
TIME_DURATION_UNITS = (
    ('week', 60 * 60 * 24 * 7),
    ('day', 60 * 60 * 24),
    ('hour', 60 * 60),
    ('min', 60),
    ('sec', 1)
)
async def _human_time_duration(seconds):
    if seconds == 0:
        return 'inf'
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append('{} {}{}'
                         .format(amount, unit, "" if amount == 1 else "s"))
    return ', '.join(parts)

@nikki.on_message(filters.command("ping", [".", "!","#"]) & filters.user(SUDO_USERS) & ~filters.edited)
async def ping_pong(_, message: Message):
        #await message.reply_chat_action("typing")
        start = time()
        m_reply = await eor(message,"checking ping...")
        delta_ping = time() - start
        current_time = datetime.utcnow()
        uptime_sec = (current_time - START_TIME).total_seconds()
        uptime = await _human_time_duration(int(uptime_sec))
        await m_reply.edit(
        f"🏓 **PONG!!**  **{delta_ping * 1000:.3f} ms** \n"
        f"⚡️ **Uptime:** **{uptime}**\n\n "
        f"💖 ** @nikitaroy_31**"
    )


# Alive Message
@nikki.on_message(filters.command("alive", [".", "!","#"]) & filters.user(SUDO_USERS) & ~filters.edited)
async def ubalive(_, message: Message):
  start = time()
  delta_ping = time() - start
  current_time = datetime.utcnow()
  uptime_sec = (current_time - START_TIME).total_seconds()
  uptime = await _human_time_duration(int(uptime_sec))
  alive_msg = await eor(message,"`Processing...`")
  alive_pic = "driver/source/nikki.jpg"
  await message.reply_photo(alive_pic, caption=f"**🌀 Nikita Userbot is Alive 🌀** \n\n**🤖 Version** \n ↳**Bot Version:** `{ver}` \n ↳**Userbot Version:** `1.0` \n ↳**Python Version:** `{pyver}`\n ↳**Pytgcalls Version:** `{pytgver.__version__}` \n ↳**Pyrogram Version:** `{pyrover}` \n\n ↳**ping:** `⚡{delta_ping * 1000:.3f} ms ` \n ↳**Uptime:** {uptime}\n\n**🐬 Info**\n ↳**Nikki Vc Music:** @{BOT_USERNAME} \n ↳**Owner:** [Nikita Roy](tg://user?id=932498979) \n ↳**Powered by:** @{UPDATES_CHANNEL}")
  await alive_msg.delete()

#chat join 
'''
@nikki.on_message(filters.private)
async def chat_join(client: nikki, message: Message):
    invitelink = message.text
    chat_id = message.chat.id
    if "https://t.me/+" in invitelink:
        return await eor(message, 'invite link detected'
        )
  
    if invitelink.startswith("https://t.me/+"):
      invitelink = invitelink.replace(
        "https://t.me/+", "https://t.me/joinchat/"
                )
      await nikki.send_message(chat_id,'trying to join')
try:
    await nikki.join_chat(invitelink)
    except UserAlreadyParticipant:
    pass
  except Exception as e:
      LOGS.info(e)
      return await m.reply_text(
                f"❌ **userbot failed to join**\n\n**reason**: `{e}`"
            )
'''