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
            text = f"<b>○ Coder : <a href='tg://user?id={OWNER_ID}'>Ŧrαf‌αl‌g‌αrŁαw</a>\n○ Ongoing Anime : <a href='https://t.me/New_Animes_In_Hindi_Dub'>Ongoing </a>\n○ Anime Channel: <a href='https://t.me/Hindi_Anime_Dubbed_Official_16'>Anime </a>\n○ Movies Channel: <a href='https://t.me/Anime_Movie_Dubbed_In_Hindi'>Movie Hindi</a>\n○ ᴀɴɪᴍᴇ ᴄʜᴀᴛ : <a href='https://t.me/+ppmA_umDrRM5ZDc1'>ᴡᴇᴇʙ ᴢᴏɴᴇ</a></b>",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                    InlineKeyboardButton("⚡️ ᴄʟᴏsᴇ", callback_data = "close"),
                    InlineKeyboardButton('🍁 Anime Channel', url='https://t.me/New_Animes_In_Hindi_Dub')
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
