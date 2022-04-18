import os
from driver.database.dbpunish import is_gbanned_user
from driver.filters import eor, get_text
from driver.core import bot as c, user as nikki
from pyrogram import filters, Client
from pyrogram.types import Message
from config import SUDO_USERS

async def get_user_info(user):
    base_user_info = await c.get_users(user)
    # Assigning user info to vars (idk why i'm doing this)
    user_id = base_user_info.id
    first_name = base_user_info.first_name
    last_name = base_user_info.last_name
    username = base_user_info.username
    user_info = {
        "id": user_id,
        "dc": base_user_info.dc_id,
        "photo_id": base_user_info.photo.big_file_id if base_user_info.photo else None,
        "first_name": first_name if first_name else "None",
        "last_name": last_name if last_name else "None",
        "user_name": username if username else "None",
        "user_mension": base_user_info.mention,
        "is_gbanned": "Yes" if await is_gbanned_user(user_id) else "No",
        "is_sudo": "Yes" if user_id in SUDO_USERS else "No",
        "is_contact": "Yes" if base_user_info.is_contact else "No",
        "is_bot": "Yes" if base_user_info.is_bot else "No",
        "is_scam": "Yes" if base_user_info.is_scam else "No"
    }
    return user_info


@Client.on_message(filters.command("info") & ~filters.edited & ~filters.bot)
async def who_tf_is(_, message: Message):
    who_msg = await eor(message, "`Processing...`")
    r_msg = message.reply_to_message
    w_args = get_text(message)
    if r_msg:
        if r_msg.from_user:
            iuser = r_msg.from_user.id
        else:
            return await who_msg.edit("`Reply to a message from user to extract info!`")
    elif w_args:
        if w_args.isnumeric():
            iuser = int(w_args)
        else:
            iuser = w_args.replace("@", "")
    else:
        return await who_msg.edit("`Give a user id / username or reply to a message from user to extract info!`")
    # Fetching user info
    usr_info = await get_user_info(iuser)
    has_photo = usr_info["photo_id"]
    user_info_text = f"""
**︾ First Name:** `{usr_info["first_name"]}`
**︾ Last Name:** `{usr_info["last_name"]}`
**︾ User Name:** @{usr_info["user_name"]}
**︾ Mention:** {usr_info["user_mension"]}
**︾ User ID:** `{usr_info["id"]}`
**︾ DC ID:** `{usr_info["dc"]}`
**︾ Is Bot?:** `{usr_info["is_bot"]}`
**︾ Is Contact?:** `{usr_info["is_contact"]}`
**︾ Is Scam?:** `{usr_info["is_scam"]}`
**︾ Is GBanned?:** `{usr_info["is_gbanned"]}`
**︾ Is Sudo?:** `{usr_info["is_sudo"]}`
"""
    if has_photo:
        usr_dp = await _.download_media(has_photo)
        await who_msg.delete()
        await message.reply_photo(usr_dp, caption=user_info_text)
        os.remove(usr_dp)
    else:
        await who_msg.edit(user_info_text)




async def n_get_user_info(user):
    base_user_info = await nikki.get_users(user)
    # Assigning user info to vars (idk why i'm doing this)
    user_id = base_user_info.id
    first_name = base_user_info.first_name
    last_name = base_user_info.last_name
    username = base_user_info.username
    user_info = {
        "id": user_id,
        "dc": base_user_info.dc_id,
        "photo_id": base_user_info.photo.big_file_id if base_user_info.photo else None,
        "first_name": first_name if first_name else "None",
        "last_name": last_name if last_name else "None",
        "user_name": username if username else "None",
        "user_mension": base_user_info.mention,
        "is_gbanned": "Yes" if await is_gbanned_user(user_id) else "No",
        "is_sudo": "Yes" if user_id in SUDO_USERS else "No",
        "is_contact": "Yes" if base_user_info.is_contact else "No",
        "is_bot": "Yes" if base_user_info.is_bot else "No",
        "is_scam": "Yes" if base_user_info.is_scam else "No"
    }
    return user_info


@nikki.on_message(filters.command("info", [".", "!","#"]) & filters.user(SUDO_USERS) & ~filters.edited)
async def n_who_tf_is(_, message: Message):
    who_msg = await eor(message, "`Processing...`")
    r_msg = message.reply_to_message
    w_args = get_text(message)
    if r_msg:
        if r_msg.from_user:
            iuser = r_msg.from_user.id
        else:
            return await who_msg.edit("`Reply to a message from user to extract info!`")
    elif w_args:
        if w_args.isnumeric():
            iuser = int(w_args)
        else:
            iuser = w_args.replace("@", "")
    else:
        return await who_msg.edit("`Give a user id / username or reply to a message from user to extract info!`")
    # Fetching user info
    usr_info = await n_get_user_info(iuser)
    has_photo = usr_info["photo_id"]
    user_info_text = f"""
**︾ First Name:** `{usr_info["first_name"]}`
**︾ Last Name:** `{usr_info["last_name"]}`
**︾ User Name:** @{usr_info["user_name"]}
**︾ Mention:** {usr_info["user_mension"]}
**︾ User ID:** `{usr_info["id"]}`
**︾ DC ID:** `{usr_info["dc"]}`
**︾ Is Bot?:** `{usr_info["is_bot"]}`
**︾ Is Contact?:** `{usr_info["is_contact"]}`
**︾ Is Scam?:** `{usr_info["is_scam"]}`
**︾ Is GBanned?:** `{usr_info["is_gbanned"]}`
**︾ Is Sudo?:** `{usr_info["is_sudo"]}`
"""
    if has_photo:
        usr_dp = await nikki.download_media(has_photo)
        await who_msg.delete()
        await message.reply_photo(usr_dp, caption=user_info_text)
        os.remove(usr_dp)
    else:
        await who_msg.edit(user_info_text)
