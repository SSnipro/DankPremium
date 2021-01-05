import random
from telegram.ext import Dispatcher,CommandHandler
from Currency import bal

def fp(update, context):
    user = update.effective_user
    ok = random.randint(1111,3333)
    sp = ["temple 🛕. You found alot of ancient redstone contrapions 🎛 and sold them for $%s."%(ok), "dead end 💀.", "pond and a shop beside it. 🌊 If you want to buy a fishing rod and fish, use the command /PDFish 🎣."]
    d = random.choice(sp)
    msg44 = """You followed the path and found a %s

"""%(d)
    if d == sp[0]:
        bal.addcoins(user,ok)
    msg44 += "\n\nᴀᴜᴛʜᴏʀɪꜱᴇᴅ ʙʏ ɴᴏᴀʜ ❤️ \n作者：ɴᴏᴀʜ"
    update.message.reply_text(msg44)

def add_handler(dp:Dispatcher):
    fp_handler = CommandHandler('PDFollowPath', fp)
    dp.add_handler(fp_handler)

