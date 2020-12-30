import random
from telegram.ext import Dispatcher,CommandHandler
import balence

def w(update, context):
    msg = """You are exploring the wilderness when three paths lay beyond you. On the right, you see a lot of animals and luckily enough, you brought your hunting rifle.
On the left is a cliff. Down the cliff, there are some really mysterious plants. 
In front is a path. Something is telling you that you should follow it. What do you want to do?
    
/DHunt - Hunt the animals!
/DCliff - Try to get down the cliff and examine the mysterious plants!
/DFollowPath - Straight forward!
    """
    msg += "\n\nAuthorised By Noah <3\n作者：Noah"
    update.message.reply_text(msg)

def add_handler(dp:Dispatcher):
    w_handler = CommandHandler('DWilderness', w)
    dp.add_handler(w_handler)
