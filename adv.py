import random
from telegram.ext import Dispatcher,CommandHandler
import bal

def adv(update, context):
    msg = """You chose to Adventure. But now...
    
Where do you want to go?
    
/PDWilderness
/PDArctic
/PDSpace
/PDTown
/PDArea51
/PDSupremeAgency
/PDMagicalWorld
    """
    msg += "\n\nᴀᴜᴛʜᴏʀɪꜱᴇᴅ ʙʏ ɴᴏᴀʜ ❤️ \n作者：ɴᴏᴀʜ"
    update.message.reply_text(msg)

def add_handler(dp:Dispatcher):
    adv_handler = CommandHandler('PDAdventure', adv)
    dp.add_handler(adv_handler)