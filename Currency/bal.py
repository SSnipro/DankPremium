from DankPremium import config
import random
from datetime import datetime,timedelta
from telegram.ext import Dispatcher,CommandHandler, Filters
from telegram import BotCommand, Animation

#  {
#       uid:{
#           first_name: "",
#           count:0,
#           coins:0
#       }
#   }
bal = config.CONFIG['bal']

def check(user):
    uid = str(user.id)
    fname = user.first_name
    if not uid in bal:
        bal[uid] = {}
        bal[uid]['fname'] = fname
        bal[uid]['coins'] = 0
        bal[uid]['count'] = 0

def get_count(user):
    uid = str(user.id)
    return bal[uid]['count']

def get_coins(user):
    uid = str(user.id)
    return bal[uid]['coins']

def balence(update, context):
    user = update.message.from_user
    check(user)
#     update.message.reply_text("""🏦 ✨%s (银行ID: %s) 的银行账户余额：$%s ✨, %s 次取钱
# """%(user.first_name,user.id,get_coins(user),get_count(user)))
# coins_file = Path("/Users/Snipro/work/DankPremium/images/dino.gif")
    update.message.reply_text("🏦 ✨%s (银行ID: %s) 的银行账户余额：$%s ✨, %s 次取钱"%(user.first_name,user.id,get_coins(user),get_count(user)))

def addcoins(user,coins):
    uid = str(user.id)
    fname = user.first_name
    check(user)
    bal[uid]['coins'] += coins
    bal[uid]['count'] += 1
    bal[uid]['fname'] = fname
    config.CONFIG['bal'] = bal 
    config.save_config()

def add_handler(dp:Dispatcher):
    bal_handler = CommandHandler('PDBal', balence)
    dp.add_handler(bal_handler)

def get_command():
    return [BotCommand('pdbal','Check your bank account!')]