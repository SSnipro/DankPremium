import random
from telegram.ext import Dispatcher,CommandHandler
from Currency import bal

def w(update, context):
    uid = update.effective_user.id
    if 'Space Ticket' in bal.bal[uid]['inv']:
        msg = """flying... fly... fly...
        
Oh? You came past two planets you've never seen before.

Do you want to go back and explore the planets?

... or keep going?

🪐 /PDPlanets to explore the planets

✈️ /PDKeepFlying to keep flying
        """
    else: 
        msg = 'MAN YOU DONT EVEN HAVE A SPACE TICKET GET OUT OF HERE'
    msg += "\n\nᴀᴜᴛʜᴏʀɪꜱᴇᴅ ʙʏ ɴᴏᴀʜ ❤️ \n作者：ɴᴏᴀʜ"
    update.message.reply_text(msg)

def add_handler(dp:Dispatcher):
    w_handler = CommandHandler('PDFly', w)
    dp.add_handler(w_handler)