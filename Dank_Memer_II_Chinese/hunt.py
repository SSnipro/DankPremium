import random
from telegram.ext import Dispatcher,CommandHandler
import bal

def hunting(update, context):
    Hunt = ["哈哈你没有找到任何东西去捕猎", "哈哈你没有找到任何东西去捕猎", "哈哈你没有找到任何东西去捕猎", "一只熊把你吃掉了", "一只熊把你吃掉了", "你拿回来一只臭鼬并收获了 10 XP！", "你拿回来一只臭鼬并收获了 10 XP！", "你拿回来一只兔子并收获了 15 XP！", "你拿回来一只兔子并收获了 15 XP！",  "你拿回来一只兔子并收获了 15 XP！", "你拿回来一只鸭子并收获了 25 XP", "你拿回来一只鸭子并收获了 25 XP！", "你拿回来一只野猪并收获了 70 XP！", "我哩个天呐！你拿回来了一只龙并收获了 400 XP！你是咋么做到的？"]
    msg5 = random.choice(Hunt)
    if msg5 == Hunt[4] or msg5 == Hunt[5]:
        bal.bal += 10
    elif msg5 == Hunt[6] or msg5 == Hunt[7] or msg5 == Hunt[8]:
        bal.bal += 15
    elif msg5 == Hunt[9] or msg5 == Hunt[10]:
        bal.bal += 25
    elif msg5 == Hunt[11]:
        bal.bal += 70
    elif msg5 == Hunt[12]:
        bal.bal += 400
    msg5 += "\n\nAuthorised By Noah <3\n作者：Noah"
    update.message.reply_text(msg5)

def add_handler(dp:Dispatcher):
    hunt_handler = CommandHandler('DCHunt', hunting)
    dp.add_handler(hunt_handler)





