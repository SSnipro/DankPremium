import random
from telegram.ext import Dispatcher,CommandHandler
import balence

def cheap(update, context):
    shopping = ["You bought fake supplies. get rekt.", "DRILL NO WORK????????", "You made the right choice, good call! Got to your friend's research base and got 7777 XP."]
    msg = random.choice(shopping)
    msg += "\n\nAuthorised By Noah <3\n作者：Noah"
    update.message.reply_text(msg)

def add_handler(dp:Dispatcher):
    arctic_handler = CommandHandler('DCheaperStore', cheap)
    dp.add_handler(arctic_handler)
