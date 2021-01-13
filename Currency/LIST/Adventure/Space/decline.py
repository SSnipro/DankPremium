import random
from telegram.ext import Dispatcher,CommandHandler
from Currency import bal

def w(update, context):
    uid = str(update.effective_user.id)
    if not "- 🎫 Space Ticket -- [ACTIVE]" == bal.bal[uid]['inv']['items']['spaceticket']:
        msg = "You declined the offer."
    else:
        msg = "Invaid command: No offers to decline"
    msg += "\n\nᴀᴜᴛʜᴏʀɪꜱᴇᴅ ʙʏ ɴᴏᴀʜ ❤️ \n作者：ɴᴏᴀʜ"
    update.message.reply_text(msg)

def add_handler(dp:Dispatcher):
    w_handler = CommandHandler('Decline', w)
    dp.add_handler(w_handler)