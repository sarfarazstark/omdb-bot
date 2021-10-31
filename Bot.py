#sanmanasullavar errors fix akki tharanam 🙂

import pyrogram
from asyncio import sleep
from pyrogram import Client, filters
from pyrogram.types import User, Message
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from info import API_ID
from info import API_HASH
from info import BOT_TOKEN
from OMDB import get_movie_info
#=======================================================================

START_MSG = f"𝖧𝖺𝗂, \n𝖨'𝗆 𝖺 𝖲𝗂𝗆𝗉𝗅𝖾 𝖳𝖾𝗅𝖾𝗀𝗋𝖺𝗆 𝖡𝗈𝗍 𝖳𝗈 𝖦𝖾𝗍 𝖬𝗈𝗏𝗂𝖾 𝖨𝗇𝖿𝗈 𝖴𝗌𝗂𝗇𝗀 𝖮𝖬𝖣𝖻\n \n𝖲𝖾𝗇𝖽 𝖬𝖾 𝖳𝗁𝖾 𝖬𝗈𝗏𝗂𝖾 𝖭𝖺𝗆𝖾 𝖳𝗈 𝖦𝖾𝗍 𝖨𝗇𝖿𝗈 𝖠𝖻𝗈𝗎𝗍 𝖨𝗍"

STICKER = 'CAACAgUAAxkDAALjS2F9dI-C4OaXKkSgsAxjX1mkofkKAAJXBAAC6aXoV2X6ud6KqXzUHgQ'  

#=======================================================================

Sam = Client(
    session_name="OMDb-Bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

print("Starting Bot..")

#=======================================================================

@Sam.on_message(filters.command(['start']) & filters.private)
def start(client, cmd):
         cmd.reply_sticker(STICKER)
         cmd.reply_text(START_MSG)
               
@Sam.on_message(filters.text)
async def imdbcmd(client, message):
    movie_name = message.text
    movie_info = get_movie_info(movie_name)
    if movie_info:
                  poster = movie_info["pimage"]
                  urlid = movie_info['imdb_id']
                  buttons=[[InlineKeyboardButton('🎟 𝖨𝖬𝖣𝖻', url=f"https://www.imdb.com/title/{urlid}")]] 
                                                     
                  text=f"""📀 𝖳𝗂𝗍𝗅𝖾 : <b>{movie_info['title']}</b>
                            
⏱️ 𝖱𝗎𝗇𝗍𝗂𝗆𝖾 : <b>{movie_info['duration']}</b>
🌟 𝖱𝖺𝗍𝗂𝗇𝗀 : <b>{movie_info['imdb_rating']}/10</b>
🗳️ 𝖵𝗈𝗍𝖾𝗌 : <b>{movie_info['votes']}</b>

📆 𝖱𝖾𝗅𝖾𝖺𝗌𝖾 : <b>{movie_info['release']}</b>
🎭 𝖦𝖾𝗇𝗋𝖾 : <b>{movie_info['genre']}</b>
🎙 𝖫𝖺𝗇𝗀𝗎𝖺𝗀𝖾 : <b>{movie_info['language']}</b>
🌐 𝖢𝗈𝗎𝗇𝗍𝗋𝗒 : <b>{movie_info['country']}</b>

🎥 𝖣𝗂𝗋𝖾𝖼𝗍𝗈𝗋𝗌 : <b>{movie_info['director']}</b>
📝 𝖶𝗋𝗂𝗍𝖾𝗋𝗌 : <b>{movie_info['writer']}</b>
🔆 𝖲𝗍𝖺𝗋𝗌 : <b>{movie_info['actors']}</b>

🗒 𝖯𝗅𝗈𝗍 : <code>{movie_info['plot']}</code>"""
                  
                  if poster.startswith("https"):
                                                m = await message.reply_text("𝖥𝗂𝗇𝖽𝗂𝗇𝗀 𝖣𝖾𝗍𝖺𝗂𝗅𝗌..")
                                                await message.reply_photo(photo=poster.replace("_SX300","_"), caption=text, reply_markup=InlineKeyboardMarkup(buttons))
                                                await m.delete()
                  else:
                       m = await message.reply_text("𝖲𝗈𝗋𝗋𝗒,\n𝖨 𝖢𝖺𝗇'𝗍 𝖥𝗂𝗇𝖽 𝖯𝗈𝗌𝗍𝖾𝗋𝗌.\n𝖲𝖾𝗇𝖽𝗂𝗇𝗀 𝖠𝗏𝖺𝗂𝗅𝖺𝖻𝗅𝖾 𝖣𝖾𝗍𝖺𝗂𝗅𝗌..")
                       await message.reply_text(text=text, reply_markup=InlineKeyboardMarkup(buttons))
                       await sleep(4)
                       await m.delete()
    else:
        omdbbuttons=[[InlineKeyboardButton('🔍 𝖲𝖾𝖺𝗋𝖼𝗁 𝖮𝗇 𝖦𝗈𝗈𝗀𝗅𝖾.', url=f'https://google.com/search?q={movie_name.replace(" ","+")}')]]
        await message.reply_text(text="𝖢𝗈𝗎𝗅𝖽𝗇'𝗍 𝖥𝖾𝗍𝖼𝗁 𝖣𝖾𝗍𝖺𝗂𝗅𝗌\n𝖳𝗋𝗒 𝖳𝗈 𝖢𝗁𝖾𝖼𝗄 𝖸𝗈𝗎𝗋 𝖲𝗉𝖾𝗅𝗅𝗂𝗇𝗀.", reply_markup=InlineKeyboardMarkup(omdbbuttons))       


#=======================================================================
print("Bot Started!")
#=======================================================================

Sam.run()

#=======================================================================
