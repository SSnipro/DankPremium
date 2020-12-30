import random
from telegram.ext import Dispatcher,CommandHandler
import bal

def punish(update, context):
    punished = ["你表现不好，损失了 40 XP。 活该！", "你挂了。损失了 120 XP。", "哟，躲避球练的不错。这次就放过你啦！"]
    msg2 = random.choice(punished)
    if msg2 == punished[0]:
        bal.bal += -40
    elif msg2 == punished[1]:
        bal.bal += -120
    msg2 += "\n\nAuthorised By Noah <3\n作者：Noah"
    update.message.reply_text(msg2)

def add_handler(dp:Dispatcher):
    punishment_handler = CommandHandler('DCPunish', punish)
    dp.add_handler(punishment_handler)
