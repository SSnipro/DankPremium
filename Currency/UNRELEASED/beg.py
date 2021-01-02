import random
from telegram.ext import Dispatcher,CommandHandler

def begging(update, context):
    Names = ["An idiot", "Shellie", "Donald the duck", "Ur mom", "Dank Memer II", "bob", "Sus", "Danny Huang"]
    Money = random.randint(0,200)
    msg6 = ("%s donated %s XP to you! \n\nAuthorised By Noah <3\n作者：Noah"%(random.choice(Names),Money))
    update.message.reply_text(msg6)

def add_handler(dp:Dispatcher):
    beg_handler = CommandHandler('PDBeg',begging)
    dp.add_handler(beg_handler)





