import config
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
        bal[uid]['dailytime'] = datetime.now().strftime('%Y/%m/%d %H:%M:%S')
        bal[uid]['inv'] = [] 


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
    bal[uid]['dailytime'] = datetime.now().strftime('%Y/%m/%d %H:%M:%S')
    config.CONFIG['bal'] = bal 
    config.save_config()

def additem(user,t):
    check(user)
    uid = str(user.id)
    bal[uid]['inv'].append(t)
    config.CONFIG['bal'] = bal 
    config.save_config()

def get_dailytime(uid):
    return datetime.strptime(bal[uid]['dailytime'],'%Y/%m/%d %H:%M:%S')

def set_dailytime(uid,time):
    bal[uid]['dailytime']=time.strftime('%Y/%m/%d %H:%M:%S')

def daily(update,context):
    user = update.effective_user
    check(user)
    uid = str(user.id)
    username = user.username
    if datetime.now() > get_dailytime(uid):
        c = random.randint(1000,5000)
        addcoins(user,c)
        set_dailytime(uid,datetime.now() + timedelta(days=1))
        config.save_config()
        update.message.reply_text(f'Here is your ${c} daily reward @{username}!')
    else:
        update.message.reply_text("one day didn't pass yet dummy")

def inv(update,context):
    user = update.effective_user
    uid = str(user.id)
    check(user)    
    if bal[uid]['inv'] == []:
        update.message.reply_text("You have nothing in your inventory.")
    else:
        update.message.reply_text(bal[uid]['inv'])
        

def add_handler(dp:Dispatcher):
    dp.add_handler(CommandHandler('PDBal', balence))
    dp.add_handler(CommandHandler('PDDaily', daily))
    dp.add_handler(CommandHandler('PDInv', inv))

def get_command():
    return [BotCommand('pdbal','Check your bank account!'),('pddaily','Claim your daily coins!')]