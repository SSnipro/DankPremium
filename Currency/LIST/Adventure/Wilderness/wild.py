import random
from telegram.ext import Dispatcher,CommandHandler
from Currency import bal

def w(update, context):
    msg = """You've decided to explore the wilderness.

You are exploring the wilderness when three paths lay beyond you. 

➡️ On the right, you see a lot of animals and luckily enough, you brought your hunting rifle.

⬅️ On the left is a cliff. Down the cliff, there are some really mysterious plants. 

➬ In front is a path. Something is telling you that you should follow it. What do you want to do?
    
🔫 /PDHunt - Hunt the animals!
🧗🏼‍♀️ /PDCliff - Try to get down the cliff and examine the mysterious plants!
🛣 /PDFollowPath - Go straight forward!
    """
    msg += "\n\nᴀᴜᴛʜᴏʀɪꜱᴇᴅ ʙʏ ɴᴏᴀʜ ❤️ \n作者：ɴᴏᴀʜ"
    update.message.reply_text(msg)

def add_handler(dp:Dispatcher):
    w_handler = CommandHandler('PDWilderness', w)
    dp.add_handler(w_handler)