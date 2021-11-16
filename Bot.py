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

START_MSG = f"Hii , \n I'm a Simple Telegram Bot To Get Movie Info Using OMDb \n \nSend Me The **Movie Name** To Get Info About It"

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
                  buttons=[[InlineKeyboardButton('🎟 IMDb', url=f"https://www.imdb.com/title/{urlid}")]] 
                                                     
                  text=f"""📀 Title : <b>{movie_info['title']}</b>
                            
⏱️ Runtime : <b>{movie_info['duration']}</b>
🌟 Rating : <b>{movie_info['imdb_rating']}/10</b>
🗳️ Votes : <b>{movie_info['votes']}</b>

📆 Release : <b>{movie_info['release']}</b>
🎭 Genre : <b>{movie_info['genre']}</b>
🎙 Language : <b>{movie_info['language']}</b>
🌐 Country : <b>{movie_info['country']}</b>

🎥 Director : <b>{movie_info['director']}</b>
📝 Writer's : <b>{movie_info['writer']}</b>
🔆 Star's : <b>{movie_info['actors']}</b>

🗒 Plot : <code>{movie_info['plot']}</code>"""
                  
                  if poster.startswith("https"):
                                                m = await message.reply_text("Finding Details..")
                                                await message.reply_photo(photo=poster.replace("_SX300","_"), caption=text, reply_markup=InlineKeyboardMarkup(buttons))
                                                await m.delete()
                  else:
                       m = await message.reply_text("Sorry,\nI Can't Find Posters.\nSending Available Details..")
                       await message.reply_text(text=text, reply_markup=InlineKeyboardMarkup(buttons))
                       await sleep(4)
                       await m.delete()
    else:
        omdbbuttons=[[InlineKeyboardButton('🔍 Search On Google.', url=f'https://google.com/search?q={movie_name.replace(" ","+")}')]]
        await message.reply_text(text="Couldn't Fetch Details\nTry To Check Your Spelling.", reply_markup=InlineKeyboardMarkup(omdbbuttons))       


#=======================================================================
print("Bot Started!")
#=======================================================================

Sam.run()

#=======================================================================
