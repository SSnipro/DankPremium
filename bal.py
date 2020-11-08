import random
from datetime import datetime,timedelta
from telegram.ext import Dispatcher,CommandHandler, Filters

#  {
#       user:{
#           count:0,
#           coins:0
#       }
#   }
bal = {}

def check(user):
    if not user in bal.keys():
        bal[user] = {} 
        bal[user]['coins'] = 0
        bal[user]['count'] = 0

def balence(update, context,):
    user = update.message.from_user
    check(user)
    # print(bal)
    print(bal.keys())
    update.message.reply_text("""Balence of %s (ID:%s) %s attempts: %s XP
"""%(user.first_name,user.id,bal[user]['count'],bal[user]['coins']))

def addcoins(user, coins):
    check(user)
    bal[user]['coins'] += coins
    bal[user]['count'] += 1


def add_handler(dp:Dispatcher):
    bal_handler = CommandHandler('PDBal', balence)
    dp.add_handler(bal_handler)
