"""
Video + Music Stream Telegram Bot
Copyright (c) 2022-present levina=lab <https://github.com/levina-lab>

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but without any warranty; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program. If not, see <https://www.gnu.org/licenses/licenses.html>
"""


import asyncio

from config import BOT_USERNAME, SUDO_USERS

from program import LOGS
from program.utils.function import get_calls

from driver.queues import QUEUE, clear_queue
from driver.core import user, me_bot, calls
from driver.filters import command, other_filters
from driver.database.dbchat import remove_served_chat
from driver.database.dbqueue import remove_active_chat
from driver.decorators import authorized_users_only, bot_creator, check_blacklist, sudo_users_only

from pyrogram.types import Message
from pyrogram import Client, filters
from pyrogram.raw.types import InputPeerChannel
from pyrogram.raw.functions.phone import CreateGroupCall, DiscardGroupCall
from pyrogram.errors import UserAlreadyParticipant, UserNotParticipant, ChatAdminRequired


@Client.on_message(
    command(["userbotjoin", f"userbotjoin@{BOT_USERNAME}"]) & other_filters
)
@check_blacklist()
@authorized_users_only
@bot_creator
@sudo_users_only
async def join_chat(c: Client, m: Message):
    chat_id = m.chat.id
    try:
        invitelink = (await c.get_chat(chat_id)).invite_link
        if not invitelink:
            await c.export_chat_invite_link(chat_id)
            invitelink = (await c.get_chat(chat_id)).invite_link
        if invitelink.startswith("https://t.me/+"):
            invitelink = invitelink.replace(
                "https://t.me/+", "https://t.me/joinchat/"
            )
        await user.join_chat(invitelink)
        await remove_active_chat(chat_id)
        return await user.send_message(chat_id, "✅ userbot joined this chat")
    except UserAlreadyParticipant:
        return await user.send_message(chat_id, "✅ userbot already in this chat")


@Client.on_message(
    command(["userbotleave", f"userbotleave@{BOT_USERNAME}"]) & other_filters
)
@check_blacklist()
@authorized_users_only
@bot_creator
@sudo_users_only
async def leave_chat(c :Client, m: Message):
    chat_id = m.chat.id
    try:
        if chat_id in QUEUE:
            await remove_active_chat(chat_id)
            await user.leave_chat(chat_id)
            return await c.send_message(chat_id, "✅ userbot has left from chat")
        else:
            await user.leave_chat(chat_id)
            return await c.send_message(chat_id, "✅ userbot has left from chat")
    except UserNotParticipant:
        return await c.send_message(chat_id, "❌ userbot already leave chat")


@Client.on_message(command(["leaveall", f"leaveall@{BOT_USERNAME}"]) & ~filters.edited)
@bot_creator
@sudo_users_only
async def leave_all(c: Client, message: Message):
    if message.from_user.id not in SUDO_USERS:
        return
    run_1 = 0
    run_2 = 0
    msg = await message.reply("🔄 Userbot started leaving all groups")
    async for dialog in user.iter_dialogs():
        try:
            await user.leave_chat(dialog.chat.id)
            await remove_active_chat(dialog.chat.id)
            run_1 += 1
            await msg.edit(
                f"Userbot leaving...\n\nLeft from: {run_1} chats.\nFailed in: {run_2} chats."
            )
        except Exception:
            run_2 += 1
            await msg.edit(
                f"Userbot leaving...\n\nLeft from: {run_1} chats.\nFailed in: {run_2} chats."
            )
        await asyncio.sleep(0.7)
    await msg.delete()
    await c.send_message(
        message.chat.id, f"✅ Left from: {run_2} chats.\n❌ Failed in: {run_2} chats."
    )


@Client.on_message(command(["startvc", f"startvc@{BOT_USERNAME}"]) & other_filters)
@check_blacklist()
@authorized_users_only
@bot_creator
@sudo_users_only
async def start_group_call(c: Client, m: Message):
    chat_id = m.chat.id
    msg = await c.send_message(chat_id, "`starting...`")
    try:
        peer = await user.resolve_peer(chat_id)
        await user.send(
            CreateGroupCall(
                peer=InputPeerChannel(
                    channel_id=peer.channel_id,
                    access_hash=peer.access_hash,
                ),
                random_id=user.rnd_id() // 9000000000,
            )
        )
        await msg.edit_text("✅ Group call started !")
    except ChatAdminRequired:
        await msg.edit_text(
            "The userbot is not admin in this chat. To start the Group call you must promote the userbot as admin first with permission:\n\n» ❌ manage_video_chats"
        )


@Client.on_message(command(["stopvc", f"stopvc@{BOT_USERNAME}"]) & other_filters)
@check_blacklist()
@authorized_users_only
@bot_creator
@sudo_users_only
async def stop_group_call(c: Client, m: Message):
    chat_id = m.chat.id
    msg = await c.send_message(chat_id, "`stopping...`")
    try:
        if not (
            group_call := (
                await get_calls(m, err_msg="group call not active")
            )
        ):
            await msg.edit_text("❌ The group call already ended")
            return
        await user.send(
            DiscardGroupCall(
                call=group_call
            )
        )
        await msg.edit_text("✅ Group call has ended !")
    except Exception as e:
        if "GROUPCALL_FORBIDDEN" in str(e):
            await msg.edit_text(
                "The userbot is not admin in this chat. To stop the Group call you must promote the userbot as admin first with permission:\n\n» ❌ manage_video_chats"
            )


@Client.on_message(filters.left_chat_member)
async def bot_kicked(c: Client, m: Message):
    bot_id = me_bot.id
    chat_id = m.chat.id
    left_member = m.left_chat_member
    if left_member.id == bot_id:
        if chat_id in QUEUE:
            await remove_active_chat(chat_id)
            await calls.leave_group_call(chat_id)
            clear_queue(chat_id)
            return
        try:
            await user.leave_chat(chat_id)
            await remove_served_chat(chat_id)
        except Exception as e:
            LOGS.info(e)
