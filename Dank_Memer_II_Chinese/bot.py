import random
from telegram.ext import Dispatcher,CommandHandler
from telegram.ext import Updater
from telegram.ext import MessageHandler, Filters
import os
import reward
import punz
import fishy
import search
import hunt
import begg
import guessnum
import solvec
import bal

def start(update, context):
    update.message.reply_text("""
    Hallo！！！我叫ᴅᴀɴᴋɪɪ。由伟大的 Noah创造。
    ᴅᴀɴᴋɪɪ 提供了许多有趣的功能。您可以做很多事情来尝试获得更多XP！
    
    你还可以四处乱搞。 
    
    此外，Noah会很快尝试添加一些新功能！
    
    玩得开心哦！
    
    --------------------
    指令：
    
    /DCReward：获取每日奖励！
    /DCPunish：别惹麻烦!
    /DCSearch：搜寻XP区域时要小心！
    /DCFish：嗯...我想知道海底有什么东西... 
    /DCHunt： 狩猎一些动物，并获得一些免费的XP！请提防熊…… 
    /DCBeg: 讨钱吧穷人
    /DCGuess (空格 0～100里的一个数字）猜对了有奖励呦！
    /DCSolve [数字1] [加/减/乘/除] [数字2] 回去做数学作业去！
    --------------------
    """)

def read_file_as_str(file_path): 
    if not os.path.isfile(file_path):
        raise TypeError(file_path + " does not exist")
    all_the_text = open(file_path).read()
    return all_the_text

TOKEN = read_file_as_str('TOKEN4')
print (TOKEN)
updater = Updater(token=TOKEN, use_context=True)
dispatcher = updater.dispatcher
start_handler = CommandHandler('DCStart', start)
info_handler = CommandHandler('DCInfo', start)
dispatcher.add_handler(start_handler)
dispatcher.add_handler(info_handler)
begg.add_handler(dispatcher)
reward.add_handler(dispatcher)
punz.add_handler(dispatcher)
fishy.add_handler(dispatcher)
search.add_handler(dispatcher)
hunt.add_handler(dispatcher)
guessnum.add_handler(dispatcher)
bal.add_handler(dispatcher)
solvec.add_handler(dispatcher)
updater.start_polling()
