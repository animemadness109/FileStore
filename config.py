#(©)Codeflix_Bots




import os
import logging
from logging.handlers import RotatingFileHandler



#Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "7251295977:AAEFULfhETjhwwK4O7o_JPqYJlGMDcYHkhs")

#Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "28713982"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "237e15f7c006b10b4fa7c46fee7a5377")

#Your db channel Id
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002200969951"))

#OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "7195990500"))

#Port
PORT = os.environ.get("PORT", "8080")

#Database 
DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://Mrdaxx123:Mrdaxx123@cluster0.q1da65h.mongodb.net/?retryWrites=true&w=majority")
DB_NAME = os.environ.get("DATABASE_NAME", "Cluser0")

#force sub channel id, if you want enable force sub
FORCE_SUB_CHANNEL_1 = int(os.environ.get("FORCE_SUB_CHANNEL_1", "-1002105769442"))
FORCE_SUB_CHANNEL_2 = int(os.environ.get("FORCE_SUB_CHANNEL_2", "-1002027971137"))
FORCE_SUB_CHANNEL_3 = int(os.environ.get("FORCE_SUB_CHANNEL_3", "-1002052881308"))
FORCE_SUB_CHANNEL_4 = int(os.environ.get("FORCE_SUB_CHANNEL_4", "-1001940231860"))


TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

START_PIC = os.environ.get("START_PIC", "http://telegra.ph/file/4ca23dac2305a53868a35.jpg")
FORCE_PIC = os.environ.get("FORCE_PIC", "http://telegra.ph/file/53757d552ea0f75fbc013.jpg")

#start, help about message
HELP_TXT = "<b>1. First Join the channel \n2. Tap on Original link again or Reload  \n3. Tap on Start and Done ✅.</b>"
ABOUT_TXT = "<b>○ ᴏᴡɴᴇʀ : <a href='tg://user?id={OWNER_ID}'>Ŧrαf‌αl‌g‌αrŁαw</a>\n○ Ongoing Anime : <a href='https://t.me/Ongoing_Madness'>Ongoing Madness</a>\n○ Anime Channel: <a href='https://t.me/Anime_Madness'>Anime Madness</a>\n○ Movies Channel: <a href='https://t.me/Madness_Movie'>Movie Madness</a>\n○ ᴀɴɪᴍᴇ ᴄʜᴀᴛ : <a href='https://t.me/Weebs_Madness'>ᴡᴇᴇʙ ᴢᴏɴᴇ</a></b>"
START_MSG = os.environ.get("START_MESSAGE", "<b>ʜᴇʟʟᴏ.{first}\n\n ɪ ᴀᴍ ᴍᴜʟᴛɪ ғɪʟᴇ sᴛᴏʀᴇ ʙᴏᴛ , ɪ ᴄᴀɴ sᴛᴏʀᴇ ᴘʀɪᴠᴀᴛᴇ ғɪʟᴇs ɪɴ sᴘᴇᴄɪғɪᴇᴅ ᴄʜᴀɴɴᴇʟ ᴀɴᴅ ᴏᴛʜᴇʀ ᴜsᴇʀs ᴄᴀɴ ᴀᴄᴄᴇss ɪᴛ ғʀᴏᴍ sᴘᴇᴄɪᴀʟ ʟɪɴᴋ » @Anime_Madness</b>")
try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "7195990500 6321766718").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")

#Force sub message 
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "𝙺𝚘𝚗𝚒𝚌𝚑𝚒𝚠𝚊 {first}⚡ 🫧ᴘʟᴇᴀꜱᴇ ᴊᴏɪɴ ʙᴏᴛʜ ᴏꜰ ᴏᴜʀ ᴀɴɪᴍᴇ ᴄʜᴀɴɴᴇʟꜱ ᴀɴᴅ ᴛʀʏ ᴀɢᴀɪɴ...!!")

#set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", "<b>» ʙʏ @Anime_Madness</b>")

#set True if you want to prevent users from forwarding files from bot
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "True" else False

#Set true if you want Disable your Channel Posts Share button
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True'

BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "ʙᴀᴋᴋᴀ ! ʏᴏᴜ ᴀʀᴇ ɴᴏᴛ ᴍʏ ꜱᴇɴᴘᴀɪ!!\n\n» ᴍʏ ᴏᴡɴᴇʀ : @LUFFY1JOYBOY"

ADMINS.append(OWNER_ID)
ADMINS.append(7195990500)

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
