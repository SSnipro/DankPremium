import random
from telegram.ext import Dispatcher,CommandHandler
from Currency import bal


def pog(update, context):
    msg44 = """What do you want to do with your life? 
    
/PDAdventure 冒险 
/PDWork 工作
/PDStudy 学习
/PDSearch 探索
    """
    msg44 += "\n\nAuthorised By Noah <3\n作者：Noah"
    update.message.reply_text(msg44)

def add_handler(dp:Dispatcher):
    list_handler = CommandHandler('PDList', pog)
    dp.add_handler(list_handler)

