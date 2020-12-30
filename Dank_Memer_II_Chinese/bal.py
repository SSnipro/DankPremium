import random
from telegram.ext import Dispatcher,CommandHandler
ppl = {}
bal = 0
def balence(update, context):
    user = update.message.from_user.first_name
    global ppl
    global bal
    print ("%s, %s, %s"%(ppl,bal,user))
    ppl[user] = bal
    update.message.reply_text("""Balences:

%s - %s XP

    """%(user,ppl[user]))
def add_handler(dp:Dispatcher):
    bal_handler = CommandHandler('DCBal', balence)
    dp.add_handler(bal_handler)
