import random, math
from telegram.ext import Dispatcher,CommandHandler

def TwFgame(update,context): 
    # cards = [A,2,3,4,5,6,7,8,9,10,J,Q,K]
    cards = [1,2,3,4,5,6,7,8,9,10,10,10,10]
    card1 = random.choice(cards)
    card2 = random.choice(cards)
    card3 = random.choice(cards)
    card4 = random.choice(cards)
    reply = f"The numbers are: {card1}, {card2}, {card3}, and {card4}"
    symbols = [r"+","-",r"*","/"]
    for i in range(0,3):
        for j in range(0,3):
            for k in range(0,3):
                for s1 in symbols:
                    for s2 in symbols:
                        for s3 in symbols:
                            s123TransInt = [s1,s2,s3]
                            fstring = f"{card1}{s1}{card2}{s2}{card3}{s3}{card4}"
                            strTransInt = str(fstring)
                            final = strTransInt
                         
    # if count == 24:
    #     answer += "%s %s %s %s %s %s %s = %s\n"%(a,one,b,two,c,three,d,count)
    #     update.message.reply_text(answer)
    # # elif count == False:
    #     answer += "Impossible combination!\n"
    update.message.reply_text(reply)   


def add_handler(dp:Dispatcher):
    blackjack_handler = CommandHandler('pdtwf', TwFgame)
    dp.add_handler(blackjack_handler)
             