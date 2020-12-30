import random
from telegram.ext import Dispatcher,CommandHandler
from telegram import BotCommand
import bal

def fish(update, context):
    Fish = [
        "💥 LOL You got nothing, git gud. \n\n💥 哈哈哈钓了一天鱼都没钓着。回家修炼去吧！",
        "💥 LOL You got nothing, git gud. \n\n💥 哈哈哈钓了一天鱼都没钓着。回家修炼去吧！", 
        "💥 LOL You got nothing, git gud. \n\n💥 哈哈哈钓了一天鱼都没钓着。回家修炼去吧！", 
        "💥 LOL You got nothing, git gud. \n\n💥 哈哈哈钓了一天鱼都没钓着。回家修炼去吧！", 
        "💥 LOL You got nothing, git gud. \n\n💥 哈哈哈钓了一天鱼都没钓着。回家修炼去吧！", 
        "💥 LOL You got nothing, git gud. \n\n💥 哈哈哈钓了一天鱼都没钓着。回家修炼去吧！",  
        "🐠 You brought one common fish and gained $5! \n\n🐠 你钓到了一条太阳鱼，收获了 $5。",
        "🐠 You brought one common fish and gained $5! \n\n🐠 你钓到了一条太阳鱼，收获了 $5。",
        "🐠 You brought one common fish and gained $5! \n\n🐠 你钓到了一条太阳鱼，收获了 $5。",
        "🐠 You brought one common fish and gained $5! \n\n🐠 你钓到了一条太阳鱼，收获了 $5。",
        "🐠🐠 You brought back two common fishes and gained $10! \n\n🐠🐠 你钓到了两条太阳鱼，收获了 $10。",
        "🐠🐠 You brought back two common fishes and gained $10! \n\n🐠🐠 你钓到了两条太阳鱼，收获了 $10。",
        "🐠🐠 You brought back two common fishes and gained $10! \n\n🐠🐠 你钓到了两条太阳鱼，收获了 $10。",
        "4x🐠 You brought back four common fishes and gained $20! \n\n4x🐠 你钓到了四条太阳鱼，收获了 $20。", 
        "🐟 You brought back one RARE fish and gained $100! Whoo Hoo! \n\n🐟 你钓到了一条 大嘴鲈鱼 ，收获了 $100。棒棒哒～ ", 
        "🐟 You brought back one RARE fish and gained $100! Whoo Hoo! \n\n🐟 你钓到了一条 大嘴鲈鱼 ，收获了 $100。棒棒哒～ ", 
        "💳 You fished up a credit card and gave it to the police. You gained $700. Wait what just happened? \n\n💳 你钓到一张银行卡并交给了警察。你得到了 $700。等会等会，发生了什么?!"
        ]
    msg3 = random.choice(Fish)
    user = update.message.from_user
    if msg3 == Fish[6] or msg3 == Fish[7] or msg3 == Fish[8] or msg3 == Fish[9]:
        bal.addcoins(user,5)
    elif msg3 == Fish[12] or msg3 == Fish[10] or msg3 == Fish[11]:
        bal.addcoins(user,10)
    elif msg3 == Fish[13]:
        bal.addcoins(user,20)
    elif msg3 == Fish[14] or msg3 == Fish[15]:
        bal.addcoins(user,100)
    elif msg3 == Fish[16]:
        bal.addcoins(user,700)
    msg3 += "\n\nᴀᴜᴛʜᴏʀɪꜱᴇᴅ ʙʏ ɴᴏᴀʜ ❤️ \n作者：ɴᴏᴀʜ"
    update.message.reply_text(msg3)

def add_handler(dp:Dispatcher):
    fish_handler = CommandHandler('PDFish', fish)
    dp.add_handler(fish_handler)

def get_command():
    return [BotCommand('pdfish','Try your luck with fishing!')]

