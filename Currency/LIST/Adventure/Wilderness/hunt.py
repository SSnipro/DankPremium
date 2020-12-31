import random
from telegram.ext import Dispatcher,CommandHandler
from telegram import BotCommand
from Currency import bal

def hunting(update, context):
    Hunt = [
        "💥 LOL you suck, you found nothing to hunt \n\n💥 哈哈你没有找到任何东西去捕猎", 
        "💥 LOL you suck, you found nothing to hunt \n\n💥 哈哈你没有找到任何东西去捕猎", 
        "💥 LOL you suck, you found nothing to hunt \n\n💥 哈哈你没有找到任何东西去捕猎", 
        "🐻 A bear almost ate you. You lost $250. \n\n🐻 一只熊差点把你吃掉了。你失去了 $250。", 
        "🐻 A bear almost ate you. You lost $250. \n\n🐻 一只熊差点把你吃掉了。你失去了 $250。", 
        "🦨 You brought back a skunk and gained $10! \n\n🦨 你拿回来一只臭鼬并收获了 $10！", 
        "🦨 You brought back a skunk and gained $10! \n\n🦨 你拿回来一只臭鼬并收获了 $10！", 
        "🐇 You brought back a rabbit and gained $15! \n\n🐇 你拿回来一只兔子并收获了 $15！", 
        "🐇 You brought back a rabbit and gained $15! \n\n🐇 你拿回来一只兔子并收获了 $15！", 
        "🐇 You brought back a rabbit and gained $15! \n\n🐇 你拿回来一只兔子并收获了 $15！", 
        "🦆 You brought back a duck and gained $25! \n\n🦆 你拿回来一只鸭子并收获了 $25!", 
        "🦆 You brought back a duck and gained $25! \n\n🦆 你拿回来一只鸭子并收获了 $25!", 
        "🐗 You brought back a boar and gained $70! \n\n🐗 你拿回来一只野猪并收获了 $70！", 
        "Holy Moly! \n🐉 You brought back a DRAGON and gained $400! How'd you even manage that? \n\n我哩个天呐！\n 🐉 你拿回来了一只龙并收获了 $400！你是咋么做到的？"]

    msg5 = random.choice(Hunt)
    user = update.message.from_user
    if msg5 == Hunt[5] or msg5 == Hunt[6]:
        bal.addcoins(user,10)
    elif msg5 == Hunt[7] or msg5 == Hunt[9] or msg5 == Hunt[8]:
        bal.addcoins(user,15)
    elif msg5 == Hunt[11] or msg5 == Hunt[10]:
        bal.addcoins(user,25)
    elif msg5 == Hunt[12]:
        bal.addcoins(user,70)
    elif msg5 == Hunt[13]:
        bal.addcoins(user,400)
    elif msg5 == Hunt[3] or msg5 == Hunt[4]:
        bal.addcoins(user,-250)

    msg5 += "\n\nᴀᴜᴛʜᴏʀɪꜱᴇᴅ ʙʏ ɴᴏᴀʜ ❤️ \n作者：ɴᴏᴀʜ"
    update.message.reply_text(msg5)

def add_handler(dp:Dispatcher):
    hunt_handler = CommandHandler('PDHunt', hunting)
    dp.add_handler(hunt_handler)


def get_command():
    return [BotCommand('pdhunt','Hunt down wild animals!')]



