import random
from telegram.ext import Dispatcher,CommandHandler
import balence

def arctic(update, context):
    msg = """You are at the arctic. A friend of yours called you and wanted you to go to the arcic research station but you need a snow-moto and a drill.
Do you want to:

Go to the cheaper store? /DCheaperStore

Or:

Go to the better store with better supplies? /DBetterStore
    """
    msg += "\n\nAuthorised By Noah <3\n作者：Noah"
    update.message.reply_text(msg)

def add_handler(dp:Dispatcher):
    arctic_handler = CommandHandler('DArctic', arctic)
    dp.add_handler(arctic_handler)
