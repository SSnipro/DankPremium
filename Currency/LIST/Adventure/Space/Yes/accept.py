import random
from telegram.ext import Dispatcher,CommandHandler
from Currency import bal

def w(update, context):
    user = update.effective_user
    uid = str(user.id)
    if not "- 🎫 Space Ticket -- [ACTIVE]" == bal.bal[uid]['inv']['items']['spaceticket']:
        if bal.bal[uid]['coins'] >= 100000:
            msg = "You accepted the offer. 'Space Ticket' is now in your inventory."
            bal.addcoins(user,-100000)
            bal.additem(user,'🎫 Space Ticket','spaceticket')
    else:
        msg = "Invaid command: No offers to accept"
        
    msg += "\n\nᴀᴜᴛʜᴏʀɪꜱᴇᴅ ʙʏ ɴᴏᴀʜ ❤️ \n作者：ɴᴏᴀʜ"
    update.message.reply_text(msg)

def add_handler(dp:Dispatcher):
    w_handler = CommandHandler('Accept', w)
    dp.add_handler(w_handler)