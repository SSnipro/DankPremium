import random
from telegram import BotCommand, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Dispatcher,CommandHandler
from Currency import bal

def pog(update, context):
    msg44 = """What do you want to do with your life? 
    
/PDAdventure ⚔️ 冒险 
/PDWork 💼 工作
/PDStudy 📝 学习
/PDSearch 🕵🏻‍♂️ 探索
    """
    msg44 += "\n\nᴀᴜᴛʜᴏʀɪꜱᴇᴅ ʙʏ ɴᴏᴀʜ ❤️ \n作者：ɴᴏᴀʜ"
    update.message.reply_text(msg44)

def add_handler(dp:Dispatcher):
    list_handler = CommandHandler('PDList', pog)
    dp.add_handler(list_handler)

def get_command():
    return [BotCommand('pdlist','A list of things you can do!')]

