import random
from telegram.ext import Dispatcher,CommandHandler
from Currency import bal

def c(update, context):
    user = update.effective_user
    ri = random.randint(2000,12000)
    choices = [
        "💥 You accidentally fell of the cliff 🧗🏼‍♀️ and broke both of your legs 🤕.", 
        "💥 You fell of the cliff 🧗🏼‍♀️ and landed hard on a rock.", 
        "😇 You successfully went down safely. You examined the plants and reported it to the scientests. The scientests had never seen such things before and you were rewarded $%s for a reward."%(ri)
        ]
    msg = random.choice(choices)
    if msg == choices[2]:
        bal.addcoins(user,ri)
    msg += "\n\nᴀᴜᴛʜᴏʀɪꜱᴇᴅ ʙʏ ɴᴏᴀʜ ❤️ \n作者：ɴᴏᴀʜ"
    update.message.reply_text(msg)

def add_handler(dp:Dispatcher):
    w_handler = CommandHandler('PDCliff', c)
    dp.add_handler(w_handler)
