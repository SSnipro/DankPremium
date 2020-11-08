import random
from telegram.ext import Dispatcher,CommandHandler
from telegram.ext import Updater
from telegram.ext import MessageHandler, Filters
import os


def start(update, context):
    update.message.reply_text("""
Sup! My name is Dank Premium. Coded by O Great Noah.
Dank Premium provides a lot of fun features. You can do many things to try to get much XP as you want!
    
Also, Noah will try to add some new feature really soon!
    
Enjoy!
    
--------------------
Commands:
 
哈喽！我叫 Dank Premium。由伟大的 Noah创造。
Dank Premium 提供了许多有趣的功能。您可以做很多事情来尝试获得更多XP！
    
你还可以四处乱搞。 
    
此外，Noah会很快尝试添加一些新功能！
    
玩得开心哦！
    
--------------------
指令：

--------------------
    """)

def read_file_as_str(file_path): 
    if not os.path.isfile(file_path):
        raise TypeError(file_path + " does not exist")
    all_the_text = open(file_path).read()
    return all_the_text

TOKEN = read_file_as_str('TOKEN%')
updater = Updater(token=TOKEN, use_context=True)
dispatcher = updater.dispatcher
start_handler = CommandHandler('PDStart', start)
info_handler = CommandHandler('PDInfo', start)
dispatcher.add_handler(start_handler)
dispatcher.add_handler(info_handler)
updater.start_polling()