#(©)Codexbotz

from pyrogram import __version__
from bot import Bot
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text = f"<b>○ ᴏᴡɴᴇʀ : <a href='tg://user?id={OWNER_ID}'>Ŧrαf‌αl‌g‌αrŁαw</a>\n○ Hentai Channel : <a href='https://t.me/+ur5FuoTlHGMzYWI1'>Hentai Madness</a>\n○ Cornhub Channel: <a href='https://t.me/+TL_dcAwR3CVjZDhl'>Cornhub Madness</a>\n○ Jav Porn Channel: <a href='https://t.me/+jEJhhzsk8I02OTI1'>Jav Madness</a>\n○ Cosplay Corn : <a href='https://t.me/+mlAPzGJqmRcxMzRl'>Cosplay ᴢᴏɴᴇ</a></b>",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                    InlineKeyboardButton("⚡️ ᴄʟᴏsᴇ", callback_data = "close"),
                    InlineKeyboardButton('🍁 Cultured Channel', url='https://t.me/Cultured_Madness')
                    ]
                ]
            )
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass
