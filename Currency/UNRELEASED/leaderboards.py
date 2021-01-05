from Currency import bal
import random
from datetime import datetime,timedelta
from telegram.ext import Dispatcher,CommandHandler, Filters
from telegram import BotCommand
import config
import json


config_file = 'my.json'

def load_config():
    with open(config_file, 'r') as configfile:
        CONFIG = json.load(configfile)
    return CONFIG

def help():
  return """ 💎 ~🚧 Function under construction 🚧~ 💎 Sorry! ~
What? Still want to check the process? Then run the command '/PDLeaderboards Currency'.

💎 ~🚧 功能施工中 🚧~ 💎 请谅解 ~
想看进度？执行命令'/PDLeaderboards Currency'。"""

def lb(update,context):
    # user = update.effective_user
    # uid = str(user.id)
    CONFIG = load_config()["bal"]
    if len(context.args) == 0 :
        update.message.reply_text(help()) 
    elif len(context.args) == 1:
        con = str(CONFIG).split('},')
        print(con)
        c = list(con)
        for i in range(1,len(c)+1):
            print(i)
            context.bot.send_message(update.effective_chat.id,text=f'#{i}: 🏦 ✨{c[i-1]}')
        
def add_handler(dp:Dispatcher):
    hunt_handler = CommandHandler('PDLeaderboards', lb)
    dp.add_handler(hunt_handler)
