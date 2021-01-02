import random
from telegram.ext import Dispatcher,CommandHandler
from telegram.ext import Updater
from telegram.ext import MessageHandler, Filters
from telegram import BotCommand
import os
from Currency import bal,work,bj,fish
from Currency.UNRELEASED import tf,lr,search
from Currency.LIST import list
from Currency.LIST.Adventure import adventure
from Currency.LIST.Adventure.Wilderness import hunt
from Fun import punish,gif
from Utils.get_file_info import animationInfo, fileInfo

def start(update, context):
    update.message.reply_text("""

Sup! My name is Dank Premium. Authorized by Telegram User SSnipro (Just call him Noah it's fine).
Dank Premium provides lots of amazing features. You can do many things to try  to get much $ as you want!
    
Also, Noah will try to add some new features really soon!
    
Enjoy!
    
--------------------
Commands:

    Currency related:

        💼 /PDWork - Submit your work to your boss. Depending on your work quality, you will either receive an reward or punishment.
        🏦 /PDBal - Check your current balence!
        🃏 /PDBJ - Play a Blackjack game against 🤖 DMII and your friends!
        🔫 /PDHunt - Hunt em down!!!!!!
        🎣 /PDFish - Try your luck by fishing!
        🎯 /PDLeaderboards - Richest people on the server! (💎 ~🚧 Function under construction 🚧~ 💎 Sorry! ~)

    Fun:

        🤡 /PDGif - Funny gifs! (💎 ~🚧 Function under construction 🚧~ 💎 Sorry! ~)
        👹 /PDPunish - get rekt in Classcraft you fool (💎 ~🚧 Function under construction 🚧~ 💎 Sorry! ~)

--------------------

哈喽！我叫 Dank Premium。由伟大的 Noah 创造。
Dank Premium 提供了许多有趣的功能。您可以做很多事情来尝试获得更多XP！
    
你还可以四处乱搞。 
    
此外，Noah 会添加一些新功能！
    
玩得开心哦！
    
--------------------
指令：

    货币：

        💼 /PDWork - 将您的工作提交给老板。 根据您的工作质量，您将获得奖励或惩罚。
        🏦 /PDBal - 检查您当前的银行账户！
        🃏 /PDBJ - 与 🤖 DMII 和您的朋友一起玩二十一点游戏！
        🔫 /PDHunt - 狩猎动物们！
        🎣 /PDFish - 试试你的运气吧！
        🎯 /PDLeaderboards - 查看服务器上的首富！(💎 ~🚧 功能施工中 🚧~ 💎 请谅解 ~)

    娱乐：

        🤡 /PDGif - 搞笑的gif文件！(💎 ~🚧 功能施工中 🚧~ 💎 请谅解 ~)
        👹 /PDPunish - 在 Classcraft 被惩罚吧哈哈 (💎 ~🚧 功能施工中 🚧~ 💎 请谅解 ~)


--------------------
    """)

def read_file_as_str(file_path): 
    if not os.path.isfile(file_path):
        raise TypeError(file_path + " does not exist")
    all_the_text = open(file_path).read()
    return all_the_text

def get_command():
    return [BotCommand('pdinfo','Information')]

TOKEN = read_file_as_str('TOKEN')
updater = Updater(token=TOKEN, use_context=True)
dispatcher = updater.dispatcher
start_handler = CommandHandler('start', start)
info_handler = CommandHandler('PDInfo', start)
dispatcher.add_handler(start_handler)
dispatcher.add_handler(info_handler)
bal.add_handler(dispatcher)
work.add_handler(dispatcher)
bj.add_handler(dispatcher)
punish.add_handler(dispatcher)
gif.add_handler(dispatcher)
tf.add_handler(dispatcher)
hunt.add_handler(dispatcher)
fish.add_handler(dispatcher)
lr.add_handler(dispatcher)
adventure.add_handler(dispatcher)
list.add_handler(dispatcher)
search.add_handler(dispatcher)
animationInfo.add_handler(dispatcher)
fileInfo.add_handler(dispatcher)

commands = work.get_command() + bal.get_command() + gif.get_command() + bj.get_command() + get_command() + hunt.get_command() + fish.get_command()
bot = updater.bot
bot.set_my_commands(commands)

updater.start_polling()