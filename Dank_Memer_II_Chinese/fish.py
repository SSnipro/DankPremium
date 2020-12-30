import random
from telegram.ext import Dispatcher,CommandHandler
import bal

def fish(update, context):
    Fish = ["哈哈哈钓了一天鱼都没钓着。回家修炼去吧！", "你钓到了一条 太阳鱼 ，收获了 5 XP。", "你钓到了两条 太阳鱼 ，收获了 10 XP。", "你钓到了四条 太阳鱼 ，收获了 20 XP。", "你钓到了一条 大嘴鲈鱼 ，收获了 100 XP。棒棒哒～ ", "你钓到一张银行卡并交给了警察。你得到了 700 XP。等会等会，发生了什么?!"]
    msg3 = random.choice(Fish)
    if msg3 == Fish[1]:
        bal.bal += 5
    elif msg3 == Fish[2]:
        bal.bal += 10
    elif msg3 == Fish[3]:
        bal.bal += 30
    elif msg3 == Fish[4]:
        bal.bal += 100
    elif msg3 == Fish[5]:
        bal.bal += 700
    msg3 += "\n\nAuthorised By Noah <3\n作者：Noah"
    update.message.reply_text(msg3)

def add_handler(dp:Dispatcher):
    fish_handler = CommandHandler('DCFish', fish)
    dp.add_handler(fish_handler)

