from pyrogram.types import *
from pyrogram.errors import *
from config import *


async def forcesub(bot, update):
        try:
            await bot.get_chat_member(AUTH_CHANNEL, update.from_user.id)
        except UserNotParticipant:
            file_id = "CAACAgUAAxkBAAEFwKpjFHLuKbwggVDodnliDlNEMPCCwAACGQcAAtzhOFaSum5URZebkCkE"
            await bot.send_sticker(update.from_user.id, file_id)
            text = FORCESUB_TEXT
            reply_markup = FORCESUB_BUTTONS
            return await bot.send_message(update.from_user.id,
            text=text,
            reply_markup=reply_markup,
            disable_web_page_preview=True)

FORCESUB_TEXT = """
        ❌Aƈƈҽʂʂ Dҽɳιҽԃ❌ 
♻️Please join our channel & 𝐓𝐫𝐲 𝐚𝐠𝐚𝐢𝐧♻️
"""

FORCESUB_BUTTONS = InlineKeyboardMarkup([[
                InlineKeyboardButton('🔰 ᴊᴏɪɴ ᴄʜᴀɴɴᴇʟ 🔰', url='https://t.me/EpicBotsSl')
            ]])
