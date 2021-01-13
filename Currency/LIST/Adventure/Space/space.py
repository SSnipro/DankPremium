import random
from telegram.ext import Dispatcher,CommandHandler
from Currency import bal

def w(update, context):
    uid = str(update.effective_user.id)
    if not "- 🎫 Space Ticket -- [ACTIVE]" == bal.bal[uid]['inv']['items']['spaceticket']:
        msg = """🚀 You arrived at the DMII rocket launch station and you wanted to buy a ticket to go to space. It costs $100000 but once you buy the ticket, you will have access to space forever. 

🙉 Do you want to buy the ticket?
        
✅ /Accept

🚫 /Decline

        """
    else:
        msg = "Ready to fly? /PDFly"
    msg += "\n\nᴀᴜᴛʜᴏʀɪꜱᴇᴅ ʙʏ ɴᴏᴀʜ ❤️ \n作者：ɴᴏᴀʜ"
    update.message.reply_text(msg)

def add_handler(dp:Dispatcher):
    w_handler = CommandHandler('PDSpace', w)
    dp.add_handler(w_handler)