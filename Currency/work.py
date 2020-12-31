import random
from telegram.ext import Dispatcher,CommandHandler
from telegram import BotCommand
from Currency import bal


def rewarded(update, context):
    user = update.message.from_user
    godif = random.randint(100,250)
    reward = ["☀️好样的 %s！你的老板给你了 $200."%user.first_name, "💵你在工作中收到了 $50.", "哈哈哈你什么也没有得到", "✨让神决定你的命运吧。 \n你的幸运终于来了！神给予了你 $%s 。"%(godif),"☀️你收获了 $200。棒棒哒~ ", "⚡️你获得了 $50。", "你一无所成。再修炼100年吧～ ", "✨让神决定你的命运吧。 \n你的幸运终于来了！神给予了你 $%s 。"%(godif),"💥你在工作中表现不好，损失了 $40。活该！", "☄️你被老板的躲避球击中。你挂了。损失了 $120。", "🎱哟，躲避球练的不错。这次就放过你啦！"]
    msg = random.choice(reward)
    if msg == reward[0] or msg == reward[4]:
        bal.addcoins(user,200)
    elif msg == reward[1] or msg == reward[5]:
        bal.addcoins(user,50)
    elif msg == reward[2] or msg == reward[6]:
        bal.addcoins(user,0)
    elif msg == reward[3] or msg == reward[7]:
        bal.addcoins(user,godif)
    elif msg == reward[8]:
        bal.addcoins(user,-40)
    elif msg == reward[9]:
        bal.addcoins(user,-120)
    elif msg == reward[10]:
        bal.addcoins(user,0)
    msg += "\n\nᴀᴜᴛʜᴏʀɪꜱᴇᴅ ʙʏ ɴᴏᴀʜ ❤️ \n作者：ɴᴏᴀʜ"
    update.message.reply_text(msg)
    godif = random.randint(100,250)


def add_handler(dp:Dispatcher):
    reward_handler = CommandHandler('pdwork', rewarded)
    dp.add_handler(reward_handler)


def get_command():
    return [BotCommand('pdwork','Submit your work. You will either get rewarded or punished depending on your work quality.')]
