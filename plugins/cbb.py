#(©)Codexbotz

from pyrogram import version
from bot import Bot
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text = f"<b>○ Coder : <a href='tg://user?id={OWNER_ID}'>Ŧrαf‌αl‌g‌αrŁαw</a>\n○ Ongoing Anime : <a href='https://t.me/New_Animes_In_Hindi_Dub'>Ongoing Anime</a>\n○ Anime Channel: <a href='https://t.me/Hindi_Anime_Dubbed_Official_16'>Anime Madness</a>\n○ ᴀɴɪᴍᴇ ᴄʜᴀᴛ : <a href='https://t.me/+tLREzdjGCXg4NzI1'>ᴡᴇᴇʙ Chat</a></b>",
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
