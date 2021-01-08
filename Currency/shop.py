import random
from telegram.ext import Dispatcher,CommandHandler
from telegram import BotCommand
from Currency import bal


def shop(update, context):
    user = update.effective_user
    if len(context.args) == 0:
        msg = """The 🤖 DMII Market

Item name: Space Ticket | Go to /PDSpace to buy it if you don't have one!

----------------------------------------------------------

Item Number: 2 | Item name: GoldPass | Item Price: $500,000

Item Number: 3 | Item name: Crossbow | Item Price: $50,000

Item Number: 4 | Item name: Arrow | Item Price: $1,000

----------------------------------------------------------

To buy an Item, do /PDShop buy [Item Number] or [Item name] 
To buy multiple arrows at once, do /PDShop buy 4 [Number]
"""
    else:
        uid = str(user.id)
        print(context.args)
        if context.args[0] == 'buy':
            if context.args[1] == 'crossbow' or context.args[1] == '3':
                if bal.bal[uid]['coins'] >= 50000:
                    msg = 'Purchase Successful! Crossbow is now in your inventory.'
                    bal.additem(user,'Crossbow')
                    bal.addcoins(user,-50000)
                else:
                    msg = "Purchase Unsuccessful. You don't have enough coins."
            elif context.args[1] == 'goldpass' or context.args[1] == '2':
                if bal.bal[uid]['coins'] >= 500000:
                    msg = 'Purchase Successful! Goldpass is now in your inventory.'
                    bal.additem(user,'Gold Pass')
                    bal.addcoins(user,-500000)
                else:
                    msg = "Purchase Unsuccessful. You don't have enough coins."
            elif context.args[1] == 'arrow' or context.args[1] == '4':
                if len(context.args) == 3:
                    if bal.bal[uid]['coins'] >= 1000 * int(context.args[2]):
                        msg = 'Purchase Successful! %s of that item is now in your inventory.'%(context.args[2])
                        bal.addarrows(user,int(context.args[2]))
                        bal.addcoins(user,-1000*int(context.args[2]))
                    else:
                        msg = "Purchase Unsuccessful. You don't have enough coins."
                else:
                    if bal.bal[uid]['coins'] >= 1000:
                        msg = 'Purchase Successful! one arrow is now in your inventory.'
                        bal.addarrows(user,-1000)
                    else:
                        msg = "Purchase Unsuccessful. You don't have enough coins."
    msg += "\n\nᴀᴜᴛʜᴏʀɪꜱᴇᴅ ʙʏ ɴᴏᴀʜ ❤️ \n作者：ɴᴏᴀʜ"
    update.message.reply_text(msg)


def add_handler(dp:Dispatcher):
    reward_handler = CommandHandler('PDShop', shop)
    dp.add_handler(reward_handler)


def get_command():
    return [BotCommand('pdshop','shop shop')]
