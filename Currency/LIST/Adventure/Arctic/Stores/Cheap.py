import random
from telegram.ext import Dispatcher,CommandHandler
from Currency import bal

def cheap(update, context):
    shopping = ["You bought fake supplies. get rekt.", "DRILL NO WORK????????", "You made the right choice, good call! Got to your friend's research base and earned 7777 XP."]
    msg = random.choice(shopping)
    msg += "\n\n\n\nᴀᴜᴛʜᴏʀɪꜱᴇᴅ ʙʏ ɴᴏᴀʜ ❤️ \n作者：ɴᴏᴀʜ"
    update.message.reply_text(msg)

def add_handler(dp:Dispatcher):
    arctic_handler = CommandHandler('PDCheaperStore', cheap)
    dp.add_handler(arctic_handler)
