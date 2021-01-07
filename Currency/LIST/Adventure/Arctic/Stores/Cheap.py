import random
from telegram.ext import Dispatcher,CommandHandler
from Currency import bal

def cheap(update, context):
    user = update.effective_user
    shopping = [
        "💥 You bought fake supplies. Get rekt.", 
        "🚱 DRILL NO WORK????????", 
        "✅ You made the right choice, good call! Got to your friend's research base and earned $7777."]
    msg = random.choice(shopping)
    if msg == shopping[2]:
        bal.addcoins(user,7777)
    msg += "\n\nᴀᴜᴛʜᴏʀɪꜱᴇᴅ ʙʏ ɴᴏᴀʜ ❤️ \n作者：ɴᴏᴀʜ"
    update.message.reply_text(msg)

def add_handler(dp:Dispatcher):
    arctic_handler = CommandHandler('PDCheaperStore', cheap)
    dp.add_handler(arctic_handler)
