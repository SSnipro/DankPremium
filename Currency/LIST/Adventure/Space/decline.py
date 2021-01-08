import random
from telegram.ext import Dispatcher,CommandHandler
from Currency import bal

def w(update, context):
    msg = "You declined."
    msg += "\n\nᴀᴜᴛʜᴏʀɪꜱᴇᴅ ʙʏ ɴᴏᴀʜ ❤️ \n作者：ɴᴏᴀʜ"
    update.message.reply_text(msg)

def add_handler(dp:Dispatcher):
    w_handler = CommandHandler('Decline', w)
    dp.add_handler(w_handler)