import random
from telegram.ext import Dispatcher,CommandHandler
from telegram import BotCommand
from Currency import bal

def punish(update, context):
    punished = ["You lost 40 XP for not behaving well. 你表现不好，损失了 40 XP。 活该！", "You died. You lost 120 XP. 你挂了。损失了 120 XP。", "You dodged and didn't get punished. 哟，躲避球练的不错。这次就放过你啦！"]
    msg2 = random.choice(punished)
    msg2 += "\n\nAuthorised By Noah <3\n作者：Noah"
    update.message.reply_text(msg2)

def add_handler(dp:Dispatcher):
    punishment_handler = CommandHandler('PDPunish', punish)
    dp.add_handler(punishment_handler)

def get_command():
    return [BotCommand('pdpunish','Ha get punished you fool')]
