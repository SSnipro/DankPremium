import bal
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
    CONFIG = load_config()
    if len(context.args) == 0 :
        update.message.reply_text(help()) 
    elif len(context.args) == 1:
        update.message.reply_text('%s'%(CONFIG))
    
def add_handler(dp:Dispatcher):
    hunt_handler = CommandHandler('PDLeaderboards', lb)
    dp.add_handler(hunt_handler)
