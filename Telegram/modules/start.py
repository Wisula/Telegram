import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

import os


import pyrogram
logging.getLogger("pyrogram").setLevel(logging.WARNING)

from database.blacklist import check_blacklist
from database.userchats import add_chat

from fsub import ForceSub



from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

UPDATES_CHANNEL = "CGSUPDATES"

btn = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton("UPDATES 📢", url="https://t.me/CGSUPDATES"),
        InlineKeyboardButton("SUPPORT 💬", url="https://t.me/CGSsupport")
        ],[
        InlineKeyboardButton("help 🌟", callback="help"),
        ]]

    )

STARTREXT = """ hello welcome bot
hello
"""
    

@Client.on_message(filters.command("start"))
async def start(bot, update):
    FSub = await ForceSub(bot, update)
    if FSub == 400:
        return
    await bot.send_message(
        chat_id=update.chat.id,
        text=STARTEXT,
        reply_markup=btn,
        disable_web_page_preview=True,
        reply_to_message_id=update.message_id
    )
    
import os
from pyrogram import Client as app
from pyrogram.errors import UserNotParticipant
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# Call backs @CGSUPDATES 
