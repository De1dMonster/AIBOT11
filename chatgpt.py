from pyrogram import Client, filters,enums,idle
from pyrogram.errors import ApiIdInvalid, ApiIdPublishedFlood, AccessTokenInvalid
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram.enums import ChatAction, ParseMode
import openai
from pyrogram.types import CallbackQuery
from config import *
import os,sys,re,requests
import asyncio,time
from random import choice
from bardapi import Bard
from datetime import datetime
import logging

FORMAT = "[DAXX] %(message)s"
logging.basicConfig(
    level=logging.WARNING, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)


StartTime = time.time()
DAXX = Client(
    "chat-gpt" ,
    api_id = API_ID,
    api_hash = API_HASH ,
    bot_token = BOT_TOKEN
)
START = f"""
❍ ʜᴇʏ, ɪ ᴀᴍ {BOT_NAME} 
❍ ᴀɴ ᴏᴘᴇɴ-ᴀɪ-ʙᴀsᴇᴅ ᴄʜᴀᴛɢᴘᴛ
❍ ɪ ᴄᴀɴ ᴀɴsᴡᴇʀ ʏᴏᴜʀ ǫᴜsᴛɪᴏɴ ᴇᴀsɪʟʏ

──────────────────
❍ ɪ ᴀᴍ ᴀᴅᴠᴀɴᴄᴇ ʙᴏᴛ ᴀɴᴅ ᴄᴀɴ 
❍ ɴsᴡᴇʀ ʏᴏᴜʀ ᴏ̨ᴜᴇʀɪᴇs ᴇᴀsʟɪʏ
❍ Rᴇᴀᴅ Tʜᴇ ʜᴇʟᴘ sᴇᴄᴛɪᴏɴ ғᴏʀ ᴍᴏʀᴇ ɪɴғᴏ
❍ ᴛᴏ ɢᴇᴛ ʜᴇʟᴘ ᴜsᴇ /help
"""
xa = bytearray.fromhex("68747470733a2f2f6769746875622e636f6d2f444158585445414d2f4441585843484154475054").decode()
SOURCE = xa
SOURCE_TEXT = f"""
❍ ʜᴇʏ, ɪ ᴀᴍ {BOT_NAME} ʙᴏᴛ
❍ ᴀɴ ᴏᴘᴇɴ-ᴀɪ-ʙᴀsᴇᴅ ᴄʜᴀᴛɢᴘᴛ
❍ ɪ ᴄᴀɴ ᴀɴsᴡᴇʀ ʏᴏᴜʀ ǫᴜᴀᴛɪᴏɴ ᴇᴀsʟɪʏ

──────────────────
❍ ᴄʟɪᴄᴋ ʙᴇʟᴏᴡ ʙᴜᴛᴛᴏɴ ☟
"""


x=["❤️"]
g=choice(x)
MAIN = [
    [
        InlineKeyboardButton(text="𝐌ᴜsɪᴄ ", url=f"https://t.me/HINATA_N_BOT"),
        InlineKeyboardButton(text=" 𝐒𝚄𝙿𝙿𝙾𝚁𝚃  ", url=f"https://t.me/T10ThiesKingsSHR"),
    ],
    [
        InlineKeyboardButton(
            text="•─╼⃝𖠁 𝐀ᴅᴅ 𝐌ᴇ 𝐁ᴀʙʏ 𖠁⃝╾─•",
            url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
        ),
    ],
    [
        InlineKeyboardButton(text="  𝐇ᴇʟᴘ & 𝐂ᴍᴅs ", callback_data="HELP"),
    ],
    [
        InlineKeyboardButton(text="𝐂ᴏɴᴛʀᴏʟʟᴇʀ ", url=f"https://t.me/NARUTO_X_ROBOT"),
        InlineKeyboardButton(text=" 𝐎ᴡɴᴇʀ  ", url=f"https://t.me/SAIF_DICTATOR"),
    ],
]
X = [
    [
        InlineKeyboardButton(text="  𝐃ɪᴄᴛᴀᴛᴏʀ ", url=f"https://t.me/SAIF_DICTATOR"),
              
        InlineKeyboardButton(text="  𝐒𝚄𝙿𝙿𝙾𝚁𝚃  ", url=f"https://t.me/T10ThiesKingsSHR"),
    ]
    ]
    
PNG_BTN = [
    [
         InlineKeyboardButton(
             text="•─╼⃝𖠁 𝐀ᴅᴅ 𝐌ᴇ 𝐁ᴀʙʏ 𖠁⃝╾─•❍",
             url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
         ),
     ],
     [
         InlineKeyboardButton(text=" 𝐒𝚄𝙿𝙿𝙾𝚁𝚃 ", 
                              url=f"https://t.me/T10ThiesKingsSHR",
         ),
     ],
]
SOURCE_BUTTONS = InlineKeyboardMarkup([[InlineKeyboardButton('𝐑ᴇᴘᴏ' , url=f"github.com/Saifdead")]])
HELP_READ = "**➤ ᴜsᴀɢᴇ** /Gojo <prompt>\n\n ʜᴇʟᴘ: `/Gojo ʜᴏᴡ ᴀʀᴇ ʏᴏᴜ ?`\n\n**➤ ᴜsᴀɢᴇ** : /ɢᴇɴᴇʀᴀᴛᴇ <prompt> \nᴇxᴀᴍᴘʟᴇ: `/ɢᴇɴᴇʀᴀᴛᴇ ᴀ ᴄᴜᴛᴇ ʙᴀʙʏ `  \n\➤ ᴜsᴀɢᴇ /lyrics : ʀᴇᴘʟʏ ᴛᴏ ᴀᴜᴅɪᴏ ꜰɪʟᴇ ᴛᴏ ᴅᴇᴛᴇᴄᴛ ʟʏʀɪᴄꜱ**➤ ᴜsᴀɢᴇ /ping ᴛᴏ ᴄʜᴇᴄᴋ ᴛʜᴇ ᴘɪɴɢ ᴏғ ᴛʜᴇ ʙᴏᴛ.**\n\n©️ @SAIF_DICTATOR**"
HELP_BACK = [
     [
           InlineKeyboardButton(text="Qᴜᴇꜱᴛɪᴏɴ ᴛʜᴀᴛ ᴄʜᴀᴛɢᴘᴛ ᴄᴀɴ ꜱᴏʟᴠᴇ ", url=f"https://t.me/SAIFHELPGC"),
           
     ],
    [
           InlineKeyboardButton(text="𝐁ᴀᴄᴋ ", callback_data="HELP_BACK"),
    ],
]

SAIF = [
"https://te.legra.ph/file/a50a449627d04835832dd.jpg",
]
S=choice(SAIF)

SHELP = [
"https://te.legra.ph/file/478fdd0082c3ff05a5155.jpg",
]
H=choice(SHELP)

SPING = [
"https://te.legra.ph/file/77e80dd7b51a410cc9e9f.jpg",
]
P=choice(SPING)

RSAIF = [
"https://te.legra.ph/file/43c3b863f5a6c99a01808.jpg",
]
R=choice(RSAIF)
  
#         start
@DAXX.on_message(filters.command(["start",f"start@{BOT_USERNAME}"]))
async def start(client, m: Message):
    try:
        accha = await m.reply_text(
                        text = f"{g}")
        await asyncio.sleep(0.2)
        await accha.edit("sᴛᴀʀᴛɪɴɢ ᴀɪ ʙᴏᴛ.")
        await asyncio.sleep(0.2)
        await accha.delete()
        umm = await m.reply_sticker(
                  sticker = STKR,
        )
        await asyncio.sleep(0.3)
        await umm.delete()
        await m.reply_photo(f"{S}",
            caption=START,
            reply_markup=InlineKeyboardMarkup(MAIN),
        )
    except Exception as y:
        await m.reply(y)
#  callback 
@DAXX.on_callback_query()
async def cb_handler(Client, query: CallbackQuery):
    if query.data == "HELP":
     await query.message.edit_text(
                      text = HELP_READ,
                      reply_markup = InlineKeyboardMarkup(HELP_BACK),
     )
    elif query.data == "HELP_BACK":
            await query.message.edit(text = START,
                  reply_markup=InlineKeyboardMarkup(MAIN),
        )
    
@DAXX.on_message(filters.command(["help", f"help@{BOT_USERNAME}"], prefixes=["","+", ".", "/", "-", "?", "$"]))
async def restart(client, message):
    hmm = await message.reply_photo(f"{H}",
                        caption=HELP_READ,
                        reply_markup= InlineKeyboardMarkup(HELP_BACK),
       )
@DAXX.on_message(filters.command(['source', 'repo', 'owner'], prefixes=["","+", ".", "/", "-", "?", "$"]))
async def source(bot, m):
    
    await m.reply_photo(f"{R}", caption=SOURCE_TEXT, reply_markup=SOURCE_BUTTONS)
#  alive
@DAXX.on_message(filters.command(["ping","alive"], prefixes=["+", "/", "-", "?", "$", "&","."]))
async def ping(client, message: Message):
        start = datetime.now()
        t = "ᴀɪ ʙᴏᴛ ᴀʟɪᴠɪɴɢ..."
        txxt = await message.reply(t)
        await asyncio.sleep(0.25)
        await txxt.edit_text("ᴀɪ ʙᴏᴛ sᴛᴀʀᴛᴇᴅ......")
        await asyncio.sleep(0.35)
        await txxt.delete()
        end = datetime.now()
        ms = (end-start).microseconds / 1000
        await message.reply_photo(f"{P}",
                             caption=f"ʜᴇʏ ʙᴀʙʏ!!\n**[{BOT_NAME}](t.me/{BOT_USERNAME}) ɪꜱ ᴀʟɪᴠᴇ 🥀 ᴀɴᴅ ᴡᴏʀᴋɪɴɢ ꜰɪɴᴇ ᴡɪᴛʜ sᴘᴇᴇᴅ ᴏꜰ \n➥ `{ms}` ms\n\n**ᴍᴀᴅᴇ ᴡɪᴛʜ ❣️ ʙʏ || [sᴀɪғ](https://t.me/SAIF_DICTATOR)||",
                             reply_markup=InlineKeyboardMarkup(PNG_BTN),
       )

#  main   
openai.api_key = OPENAI_KEY
@DAXX.on_message(filters.command(["chatgpt","ai","ask","a"],  prefixes=["+", ".", "/", "-", "?", "$","#","&"]))
async def chat(bot, message):
    
    try:
        start_time = time.time()
        await bot.send_chat_action(message.chat.id, ChatAction.TYPING)
        if len(message.command) < 2:
            await message.reply_text(
            "ᴇxᴀᴍᴘʟᴇ:**\n\n`/Gojo 𝐇ᴏᴡ 𝐀ʀᴇ 𝐘ᴏᴜ ?`")
        else:
            a = message.text.split(' ', 1)[1]
            MODEL = "gpt-3.5-turbo"
            resp = openai.ChatCompletion.create(model=MODEL,messages=[{"role": "user", "content": a}],
    temperature=0.2)
            x=resp['choices'][0]["message"]["content"]
            end_time = time.time()
            telegram_ping = str(round((end_time - start_time) * 1000, 3)) + " ᴍs"
            await message.reply_text(f"{message.from_user.first_name} ᴀꜱᴋᴇᴅ:\n\n {a} \n\n {BOT_NAME} ᴀɴꜱᴡᴇʀᴇᴅ:-\n\n {x}\n\n✨ᴛɪᴍᴇ ᴛᴀᴋᴇɴ  {telegram_ping} \n\n🎉ᴘᴏᴡᴇʀᴇᴅ ʙʏ @{BOT_USERNAME} ", parse_mode=ParseMode.MARKDOWN,reply_markup=InlineKeyboardMarkup(X))     
    except Exception as e:
        await message.reply_text(f"**ᴇʀʀᴏʀ: {e} ")

#  bard 

'''bard = Bard(token=BARD_TOKEN)   
@DAXX.on_message(filters.command("bard"))
async def bard_bot(bot, message):
    try:
        start_time = time.time()
        await bot.send_chat_action(message.chat.id, ChatAction.TYPING)
        if len(message.command) < 2:
            await message.reply_text(
            "Example:**\n\n` /bard How r u? `")
        else:
            a = message.text.split(' ', 1)[1]
            response=bard.get_answer(f"{a}")["content"]
            await message.reply_text(f"{response}\n\n🎉ᴘᴏᴡᴇʀᴇᴅ ʙʏ @{BOT_USERNAME} ", parse_mode=ParseMode.MARKDOWN,reply_markup=InlineKeyboardMarkup(X))     
    except Exception as e:
        await message.reply_text(f"**ᴇʀʀᴏʀ:  {e} ")

    '''
openai.api_key = OPENAI_KEY
@DAXX.on_message(filters.command(["image","photo","img","generate"],  prefixes=["+", ".", "/", "-", "?", "$","#","&"] ))
async def chat(bot, message):
    try:
        start_time = time.time()
        await bot.send_chat_action(message.chat.id, ChatAction.UPLOAD_PHOTO)
        if len(message.command) < 2:
            await message.reply_text(
            "**Example:**\n\n`/generate A cute baby`")
        else:
            a = message.text.split(' ', 1)[1]
            response= openai.Image.create(prompt=a ,n=1,size="1024x1024")
            image_url = response['data'][0]['url']
            end_time = time.time()
            telegram_ping = str(round((end_time - start_time) * 1000, 3)) + " ᴍs"
            await message.reply_photo(image_url,caption=f"✨ᴛɪᴍᴇ ᴛᴀᴋᴇɴ {telegram_ping} ",parse_mode=ParseMode.DISABLED,reply_markup=InlineKeyboardMarkup(X)) 
    except Exception as e:
            await message.reply_text(f"**ᴇʀʀᴏʀ: **  ` {e} `")
openai.api_key = OPENAI_KEY
@DAXX.on_message(filters.command(["text","audiototext","lyrics"],  prefixes=["","+", ".", "/", "-", "?", "$","#","&"]))
async def chat(bot, message):
    
    try:
        start_time = time.time()
        await bot.send_chat_action(message.chat.id, ChatAction.TYPING)
        if message.reply_to_message and message.reply_to_message.media:
            
            m = await message.reply_to_message.download(file_name="DAXX.mp3")
            audio_file = open(m, "rb")
            transcript = openai.Audio.transcribe("whisper-1", audio_file)
            x=transcript["text"]
            end_time = time.time()
            telegram_ping = str(round((end_time - start_time) * 1000, 3)) + " ᴍs"
            await message.reply_text(f"`{x}` \n ✨ᴛɪᴍᴇ ᴛᴀᴋᴇɴ {telegram_ping}")     
    except Exception as e:
        await message.reply_text(f"**ᴇʀʀᴏʀ: **  ` {e} `")



s = bytearray.fromhex("68747470733a2f2f6769746875622e636f6d2f444158585445414d2f4441585843484154475054").decode()

if SOURCE != s:
    print("𝗸𝗮𝗿 𝗹𝗶𝘆𝗮 𝗲𝗱𝗶𝘁 𝗺𝗶𝗹 𝗴𝘆𝗮 𝘀𝘂𝗸𝗼𝗼𝗻 𝗷𝗲𝘀𝗮 𝘁𝗵𝗮 𝘄𝗲𝘀𝗮 𝗸𝗮𝗿𝗱𝗲 ` https://github.com/SAIFDEAD/AIBOT")
    sys.exit(1)  


if __name__ == "__main__":
    print(f""" {BOT_NAME} ɪs ᴀʟɪᴠᴇ!
    """)
    try:
        DAXX.start()
        
        
    except (ApiIdInvalid, ApiIdPublishedFlood):
        raise Exception("Your API_ID/API_HASH is not valid.")
    except AccessTokenInvalid:
        raise Exception("Your BOT_TOKEN is not valid.")
    print(f"""JOIN [💘💥𝗬𝗢𝗨𝗥 𝗦𝗔𝗜𝗙 𝗔𝗜 𝗕𝗢𝗧 𝗦𝗧𝗔𝗥𝗧💘💥]
    🌺🌻𝗧𝗛𝗜𝗦 𝗥𝗘𝗣𝗢 𝗠𝗔𝗗𝗘 𝗕𝗬 𝗦𝗔𝗜𝗙 🌹💖
 {BOT_NAME} ɪs ᴀʟɪᴠᴇ!  
    """)
    idle()
    DAXX.stop()
    print("𝗦𝗔𝗜𝗙 𝗔𝗜 𝗕𝗢𝗧 𝗦𝗧𝗢𝗣 !")
