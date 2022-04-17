# @nikitabots

"""
Greetings,

 ⤷ Custom greetings plugin with Ascii text art

   © @nikitaroy_31
   © @nikitabots
"""

import os
import random

from config import SUDO_USERS
from pyrogram import filters, Client
from pyrogram.types import Message
from config import SUDO_USERS
from driver.core import bot as c, user as nikki
from driver.filters import eor, get_text

# Strings collection
S = (
    "..... (¯`v´¯)♥️\n"
    ".......•.¸.•´\n"
    "....¸.•´  🅷🅸\n"
    "... (   BABYy\n"
    "☻/ \n"
    "/▌✿🌷✿\n"
    "/ \     \|/\n"
)

X = (
    ".......🦋🦋........🦋🦋\n"
    "...🦋.........🦋🦋.......🦋\n"
    "...🦋............💙..........🦋\n"
    ".....🦋🅣🅗🅐🅝🅚🅢 🦋\n"
    "....... 🦋.................🦋\n"
    "..............🦋......🦋\n"
    "...................💙\n"
)



BYE_TEXTS = [
    """
╭━━╮
┃╭╮┣┳┳━╮
┃╭╮┃┃┃┻┫
╰━━╋╮┣━╯
╱╱╱╰━╯
    """,
    """
███████████████████
█▄─▄─▀█▄─█─▄█▄─▄▄─█
██─▄─▀██▄─▄███─▄█▀█
▀▄▄▄▄▀▀▀▄▄▄▀▀▄▄▄▄▄▀
    """,
    """

░█▀▀█ █──█ █▀▀ 
░█▀▀▄ █▄▄█ █▀▀ 
░█▄▄█ ▄▄▄█ ▀▀▀
    """,
    """
▒█▀▀█ █░░█ █▀▀ 
▒█▀▀▄ █▄▄█ █▀▀ 
▒█▄▄█ ▄▄▄█ ▀▀▀
    """,
    """
🎁🐲  𝐛Ƴ𝕖  🎄💗
    """
]

GOOD_NIGHT_TEXTS = [
    """
█▀▀ █▀█ █▀█ █▀▄
█▄█ █▄█ █▄█ █▄▀

█▄░█ █ █▀▀ █░█ ▀█▀
█░▀█ █ █▄█ █▀█ ░█░
    """,
    """
╔══╗────╔╗
║╔═╬═╦═╦╝║
║╚╗║╬║╬║╬║
╚══╩═╩═╩═╝
╔═╦╦╗─╔╗╔╗
║║║╠╬═╣╚╣╚╗
║║║║║╬║║║╔╣
╚╩═╩╬╗╠╩╩═╝
────╚═╝
    """,
    """
╭━━━╮╱╱╱╱╱╱╱╭╮
┃╭━╮┃╱╱╱╱╱╱╱┃┃
┃┃╱╰╋━━┳━━┳━╯┃
┃┃╭━┫╭╮┃╭╮┃╭╮┃
┃╰┻━┃╰╯┃╰╯┃╰╯┃
╰━━━┻━━┻━━┻━━╯
╭━╮╱╭╮╱╱╱╭╮╱╭╮
┃┃╰╮┃┃╱╱╱┃┃╭╯╰╮
┃╭╮╰╯┣┳━━┫╰┻╮╭╯
┃┃╰╮┃┣┫╭╮┃╭╮┃┃
┃┃╱┃┃┃┃╰╯┃┃┃┃╰╮
╰╯╱╰━┻┻━╮┣╯╰┻━╯
╱╱╱╱╱╱╭━╯┃
╱╱╱╱╱╱╰━━╯
    """,
    """
╭━━╮╱╱╱╱╭╮
┃╭━╋━┳━┳╯┃
┃╰╮┃╋┃╋┃╋┃
╰━━┻━┻━┻━╯
╭━┳┳╮╱╭╮╭╮
┃┃┃┣╋━┫╰┫╰╮
┃┃┃┃┃╋┃┃┃╭┫
╰┻━┻╋╮┣┻┻━╯
╱╱╱╱╰━╯
    """,
    """
✮     ✯  ✯      ✮      ✯    
  ✯       ✮    ✮   ✮       ✯  
 ✯     ✮     🌛    ✯    ✯ 
   ✯      ✮     ✮       ✮   ✯
  ✯     ✯       ✯        ✮       ✮

    🌟🌠   g๏𝑜𝓭 Ⓝί𝓰𝐇t  🎯🌠
    """,
    """
｡♥️｡･ﾟ♡ﾟ･｡♥️｡･｡･｡･｡♥️｡･\n╱╱╱╱╱╱╱╭╮╱╱╱╭╮╱╭╮╭╮\n╭━┳━┳━┳╯┃╭━┳╋╋━┫╰┫╰╮\n┃╋┃╋┃╋┃╋┃┃┃┃┃┃╋┃┃┃╭┫\n┣╮┣━┻━┻━╯╰┻━┻╋╮┣┻┻━╯\n╰━╯╱╱╱╱╱╱╱╱╱╱╰━╯\n｡♥️｡･ﾟ♡ﾟ･｡♥️° ♥️｡･ﾟ♡ﾟ･
    """,
    """
♛┈⛧┈┈•༶🦋⋇⋆✦⋆⋇🦋༶•┈┈⛧┈♛\n╱╱✨╱╱✨╱╱✨╱╱✨╱╱✨╱╱✨\n╔══╗────╔╗╔═╦╦╗─╔╗╔╗\n║╔═╬═╦═╦╝║║║║╠╬═╣╚╣╚╗\n║╚╗║╬║╬║╬║║║║║║╬║║║╔╣\n╚══╩═╩═╩═╝╚╩═╩╬╗╠╩╩═╝\n──────────────╚═╝\n╱╱✨╱╱✨╱╱✨╱╱✨╱╱✨╱╱✨╱╱✨\n♛┈⛧┈┈•༶🦋⋇⋆✦⋆⋇🦋༶•┈┈⛧┈♛･
    """
]

GOOD_MORNING_TEXTS = [
    """
╭━━╮╱╱╱╱╭╮
┃╭━╋━┳━┳╯┃
┃╰╮┃╋┃╋┃╋┃
╰━━┻━┻━┻━╯
╭━┳━╮╱╱╱╱╱╱╭╮
┃┃┃┃┣━┳┳┳━┳╋╋━┳┳━╮
┃┃┃┃┃╋┃╭┫┃┃┃┃┃┃┃╋┃
╰┻━┻┻━┻╯╰┻━┻┻┻━╋╮┃
╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╰━╯
    """,
    """
🐯 ⋆ 🕊  🎀  𝒢🌸❤️𝒹 𝑀🌞𝓇𝓃𝒾𝓃𝑔  🎀  🕊 ⋆ 🐯
    """,
    """
✷  🎀  𝒢🍪🍪𝒹 𝑀🍬𝓇𝓃𝒾𝓃𝑔  🎀  ✷
    """,
    """
🍧😝  g𝕆𝐨Ⓓ  🐨🔥

┏━┳━┓╋╋╋╋╋╋┏┓
┃┃┃┃┣━┳┳┳━┳╋╋━┳┳━┓
┃┃┃┃┃╋┃┏┫┃┃┃┃┃┃┃╋┃
┗┻━┻┻━┻┛┗┻━┻┻┻━╋┓┃
╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋┗━┛
    """,
    """
♛┈⛧┈┈•༶🦋⋇⋆✦⋆⋇🦋༶•┈┈⛧┈♛\n╱╱✨╱╱✨╱╱✨╱╱✨╱╱✨╱╱✨╱╱✨\n╔══╗────╔╗──────────╔╗\n║╔═╬═╦═╦╝║╔══╦═╦╦╦═╦╬╬═╦╦═╗\n║╚╗║╬║╬║╬║║║║║╬║╔╣║║║║║║║╬║\n╚══╩═╩═╩═╝╚╩╩╩═╩╝╚╩═╩╩╩═╬╗║\n────────────────────────╚═╝\n╱╱✨╱╱✨╱╱✨╱╱✨╱╱✨╱╱✨╱╱✨\n♛┈⛧┈┈•༶🦋⋇⋆✦⋆⋇🦋༶•┈┈⛧┈♛･
    """
]

HI_TEXTS = [
    """
💣🍔  𝓗𝓘  🍫♦️
    """,
    """
██╗░░██╗██╗
██║░░██║██║
███████║██║
██╔══██║██║
██║░░██║██║
╚═╝░░╚═╝╚═╝
    """,
    """
█░█ █
█▀█ █
    """,
    """
🐟 ⋆ 🐬  🎀  𝐻𝒾  🎀  🐬 ⋆ 🐟
    """,
    """
╔╗─╔╗
║║─║║
║╚═╝╠╗
║╔═╗╠╣
║║─║║║
╚╝─╚╩╝
    """,
    """
❈★  🎀  𝐻𝒾  🎀  ★❈
    """
]

@nikki.on_message(filters.command("byy", [".", "!","#"]) & filters.user(SUDO_USERS) & ~filters.edited)
async def bye_bois(_, message: Message):
    await eor(message, random.choice(BYE_TEXTS))

@nikki.on_message(filters.command("hui", [".", "!","#"]) & filters.user(SUDO_USERS) & ~filters.edited)
async def hi_bruh(_, message: Message):
    await eor(message, random.choice(HI_TEXTS))

@nikki.on_message(filters.command("gdm", [".", "!","#"]) & filters.user(SUDO_USERS) & ~filters.edited)
async def gm_vmro(_, message: Message):
    await eor(message, random.choice(GOOD_MORNING_TEXTS))

@nikki.on_message(filters.command("gdn", [".", "!","#"]) & filters.user(SUDO_USERS) & ~filters.edited)
async def gn_vmro(_, message: Message):
    await eor(message, random.choice(GOOD_NIGHT_TEXTS))

@nikki.on_message(filters.command("what", [".", "!","#"]) & filters.user(SUDO_USERS) & ~filters.edited)
async def what_is_dis_vmro(_, message: Message):
    WHAT_CHOISES = ["Hol up! What? ( ‌❛ ‌ʖ‌❛ )", "Da what ( ‌❛ ⏥‌❛ ) ?", "Yo, what the ¯\_( ‌❛ ⏥‌❛ )_/¯", "Wait... Why me? (-’๏_๏’-)"]
    await eor(message, random.choice(WHAT_CHOISES))

@nikki.on_message(filters.command("dk", [".", "!","#"]) & filters.user(SUDO_USERS) & ~filters.edited)
async def idk_anything(_, message: Message):
    IDK_CHOISES = ["Idk ¯\_( ‌─ ⏥‌─ )_/¯", "Who tf knows ¯\_( ‌❛ ⏥‌❛ )_/¯", "da fak? Idk anything ¯\_( ‌─ .‌─ )_/¯"]
    await eor(message, random.choice(IDK_CHOISES))

@nikki.on_message(filters.command("wdf", [".", "!","#"]) & filters.user(SUDO_USERS) & ~filters.edited)
async def wtf_wtf_wtf(_, message: Message):
    WTF_CHOISES = [
        "Wtf bro ¯_(⊙︿⊙)_/¯", "Da fak? ¯_(⊙_ʖ⊙)_/¯",
        "Yo wtf (ཫ‌﹏ੂཀ‌)", "***Fake Crying ༎ຶ‿༎ຶ***"
    ]
    await eor(message, random.choice(WTF_CHOISES))

@nikki.on_message(filters.command("sad", [".", "!","#"]) & filters.user(SUDO_USERS) & ~filters.edited)
async def sad_life(_, message: Message):
    SAD_CHOISES = [
        """
        █▀▀ ▄▀▄ █▀▄ 
▄██ █▀█ █▄▀
   🥺Nikita🥺
        """,
        "You make me sad ʕ•‌ᴥ•‌ʔ", "Ah, that hurts (;•‌༚•‌)",
        "Oh no, that's sad ( ‌˃‌⌂˂‌ ‌)"
        ]
    await eor(message, random.choice(SAD_CHOISES))



@nikki.on_message(filters.command("bby", [".", "!","#"]) & filters.user(SUDO_USERS) & ~filters.edited)
async def eviral(_, message: Message):
    await eor(message,S)


@nikki.on_message(filters.command("tnx", [".", "!","#"]) & filters.user(SUDO_USERS) & ~filters.edited)
async def fox(_, message: Message):
    await eor(message,X)


@nikki.on_message(filters.command("hbday", [".", "!","#"]) & filters.user(SUDO_USERS) & ~filters.edited)
async def hbd(_, message: Message):
    "Happy birthday art."
    inpt = get_text(message)
    text = f"♥️{inpt}♥️"
    if not inpt:
        text = ""
    await eor(
        message,
        f"{text}\n\n▃▃▃▃▃▃▃▃▃▃▃\n┊ ┊ ┊ ┊ ┊ ┊\n┊ ┊ ┊ ┊ ˚✩ ⋆｡˚ ✩\n┊ ┊ ┊ ✫\n┊ ┊ ✧🎂🍰🍫🍭\n┊ ┊ ✯\n┊ . ˚ ˚✩\n........♥️♥️..........♥️♥️\n.....♥️........♥️..♥️........♥️\n...♥️.............♥️............♥️\n......♥️.....Happy.......♥️__\n...........♥️..............♥️__\n................♥️.....♥️__\n......................♥️__\n...............♥️......♥️__\n..........♥️...............♥️__\n.......♥️..Birthday....♥️\n.....♥️..........♥️..........♥️__\n.....♥️.......♥️_♥️.......♥️__\n.........♥️♥️........♥️♥️.....\n.............................................\n..... (¯`v´¯)♥️\n.......•.¸.•´STAY BLESSED\n....¸.•´      LOVE&FUN\n... (   YOU DESERVE\n☻/ THEM A LOT\n/▌✿🌷✿\n/ \     \|/\n▃▃▃▃▃▃▃▃▃▃▃\n\n{text}",
    )
@nikki.on_message(filters.command("chill", [".", "!","#"]) & filters.user(SUDO_USERS) & ~filters.edited)
async def cheer(_, message: Message):
    "cheer text art."
    await eor(
        message,
        "💐💐😉😊💐💐\n☕️ Cheer Up  🍵\n🍂 ✨ )) ✨  🍂\n🍂┃ (( * ┣┓ 🍂\n🍂┃*💗 ┣┛ 🍂 \n🍂┗━━┛  🍂🎂 For YOU  🍰\n💐💐😌😚💐💐",
    )

@nikki.on_message(filters.command("gtwl", [".", "!","#"]) & filters.user(SUDO_USERS) & ~filters.edited)
async def getwell(_, message: Message):
    "Get Well art."
    await eor(
        message, "🌹🌹🌹🌹🌹🌹🌹🌹 \n🌹😷😢😓😷😢💨🌹\n🌹💝💉🍵💊💐💝🌹\n🌹 GetBetter Soon! 🌹\n🌹🌹🌹🌹🌹🌹🌹🌹"
    )

@nikki.on_message(filters.command("luck", [".", "!","#"]) & filters.user(SUDO_USERS) & ~filters.edited)
async def luck(_, message: Message):
    "Luck art."
    await eor(
        message, "💚~🍀🍀🍀🍀🍀\n🍀╔╗╔╗╔╗╦╗✨🍀\n🍀║╦║║║║║║👍🍀\n🍀╚╝╚╝╚╝╩╝。 🍀\n🍀・・ⓁⓊⒸⓀ🍀\n🍀🍀🍀 to you💚"
    )