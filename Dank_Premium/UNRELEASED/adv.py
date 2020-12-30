import random
from telegram.ext import Dispatcher,CommandHandler
import balence

def adv(update, context):
    msg = """Where do you want to go?
    
/DWilderness
/DArctic
/DSpace
/DTown
/DArea51
/DSupremeAgency
/DMagicalWorld
    """
    msg += "\n\nAuthorised By Noah <3\n作者：Noah"
    update.message.reply_text(msg)

def add_handler(dp:Dispatcher):
    adv_handler = CommandHandler('DAdventure', adv)
    dp.add_handler(adv_handler)
