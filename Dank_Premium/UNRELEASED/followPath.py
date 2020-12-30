import random
from telegram.ext import Dispatcher,CommandHandler
import balence
def fp(update, context):
    ok = random.randint(1111,3333)
    sp = ["temple. You found alot of ancient redstone contrapions and sold them for %s XP."%(ok), "dead end.", "pond and a shop beside it. If you want to buy a fishing rod and fish, use the command /DFish."]
    d = random.choice(sp)
    msg44 = """You followed the path and found a %s

"""%(d)
    msg44 += "\n\nAuthorised By Noah <3\n作者：Noah"
    update.message.reply_text(msg44)

def add_handler(dp:Dispatcher):
    fp_handler = CommandHandler('DFollowPath', fp)
    dp.add_handler(fp_handler)

