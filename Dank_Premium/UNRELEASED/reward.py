import random
from telegram.ext import Dispatcher,CommandHandler
import balence

def rewarded(update, context):
    user = update.message.from_user.first_name
    godif = random.randint(100,250)
    reward = ["Yay you got 200 XP. Cool? 你收获了 200 XP。棒棒哒~ ", "You got 50 XP. 你获得了 50 XP。", "You got Nothing. Git Gud. 你一无所成。再修炼100年吧～ ", "Let God decide. 让神决定你的命运吧。 \nYou got lucky dunky! God has gifted you %s XP. 你的幸运终于来了！神给予了你 （上面英文版写了，懒得再写一遍了） XP。"%(godif)]
    msg = random.choice(reward)
    if not user in balence.bal:
       balence.bal[user]['coins'] = 0
       balence.bal[user]['count'] = 0
    if msg == reward[0]:
        balence.bal[user]['coins'] += 200
        balence.bal[user]['count'] += 1 
    elif msg == reward[1]:
        balence.bal[user]['coins'] += 50
        balence.bal[user]['count'] += 1 
    elif msg == reward[3]:
        balence.bal[user]['coins'] += godif
        balence.bal[user]['count'] += 1 
    msg += "\n\nAuthorised By Noah <3\n作者：Noah"
    update.message.reply_text(msg)
    godif = random.randint(100,250)


def add_handler(dp:Dispatcher):
    reward_handler = CommandHandler('DReward', rewarded)
    dp.add_handler(reward_handler)

