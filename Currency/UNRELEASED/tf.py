import random
from telegram.ext import Dispatcher,CommandHandler

def bot(update,context): 
    #1-10
    a = random.randint(1,10)
    b = random.randint(1,10)
    c = random.randint(1,10)
    d = random.randint(1,10)
    answer = "The numbers are: %s, %s, %s, %s \n\n"%(a,b,c,d)
    symbols = ["+","-","*","/"]
    for one in symbols:
        for two in symbols:
            for three in symbols:

                #
                #
                #
                #
                if one == symbols[0]:
                    if two == symbols[0]:
                        if three == symbols[0]:
                            count = a + b + c + d
                        elif three == symbols[1]:
                            count = a + b + c - d
                        elif three == symbols[2]:
                            count = a + b + c * d
                        elif three == symbols[3]:
                            count = a + b + c / d
                    elif two == symbols[1]:
                        if three == symbols[0]:
                            count = a + b - c + d
                        elif three == symbols[1]:
                            count = a + b - c - d
                        elif three == symbols[2]:
                            count = a + b - c * d
                        elif three == symbols[3]:
                            count = a + b - c / d
                    elif two == symbols[2]:
                        if three == symbols[0]:
                            count = a + b * c + d
                        elif three == symbols[1]:
                            count = a + b * c - d
                        elif three == symbols[2]:
                            count = a + b * c * d
                        elif three == symbols[3]:
                            count = a + b * c / d
                    elif two == symbols[3]:
                        if three == symbols[0]:
                            count = a + b / c + d
                        elif three == symbols[1]:
                            count = a + b / c - d
                        elif three == symbols[2]:
                            count = a + b / c * d
                        elif three == symbols[3]:
                            count = a + b / c / d
                elif one == symbols[1]:
                    if two == symbols[0]:
                        if three == symbols[0]:
                            count = a - b + c + d
                        elif three == symbols[1]:
                            count = a - b + c - d
                        elif three == symbols[2]:
                            count = a - b + c * d
                        elif three == symbols[3]:
                            count = a - b + c / d
                    elif two == symbols[1]:
                        if three == symbols[0]:
                            count = a - b - c + d
                        elif three == symbols[1]:
                            count = a - b - c - d
                        elif three == symbols[2]:
                            count = a - b - c * d
                        elif three == symbols[3]:
                            count = a - b - c / d
                    elif two == symbols[2]:
                        if three == symbols[0]:
                            count = a - b * c + d
                        elif three == symbols[1]:
                            count = a - b * c - d
                        elif three == symbols[2]:
                            count = a - b * c * d
                        elif three == symbols[3]:
                            count = a - b * c / d
                    elif two == symbols[3]:
                        if three == symbols[0]:
                            count = a - b / c + d
                        elif three == symbols[1]:
                            count = a - b / c - d
                        elif three == symbols[2]:
                            count = a - b / c * d
                        elif three == symbols[3]:
                            count = a - b / c / d
                elif one == symbols[2]:
                    if two == symbols[0]:
                        if three == symbols[0]:
                            count = a * b + c + d
                        elif three == symbols[1]:
                            count = a * b + c - d
                        elif three == symbols[2]:
                            count = a * b + c * d
                        elif three == symbols[3]:
                            count = a * b + c / d
                    elif two == symbols[1]:
                        if three == symbols[0]:
                            count = a * b - c + d
                        elif three == symbols[1]:
                            count = a * b - c - d
                        elif three == symbols[2]:
                            count = a * b - c * d
                        elif three == symbols[3]:
                            count = a * b - c / d
                    elif two == symbols[2]:
                        if three == symbols[0]:
                            count = a * b * c + d
                        elif three == symbols[1]:
                            count = a * b * c - d
                        elif three == symbols[2]:
                            count = a * b * c * d
                        elif three == symbols[3]:
                            count = a * b * c / d
                    elif two == symbols[3]:
                        if three == symbols[0]:
                            count = a * b / c + d
                        elif three == symbols[1]:
                            count = a * b / c - d
                        elif three == symbols[2]:
                            count = a * b / c * d
                        elif three == symbols[3]:
                            count = a * b / c / d
                elif one == symbols[3]:
                    if two == symbols[0]:
                        if three == symbols[0]:
                            count = a / b + c + d
                        elif three == symbols[1]:
                            count = a / b + c - d
                        elif three == symbols[2]:
                            count = a / b + c * d
                        elif three == symbols[3]:
                            count = a / b + c / d
                    elif two == symbols[1]:
                        if three == symbols[0]:
                            count = a / b - c + d
                        elif three == symbols[1]:
                            count = a / b - c - d
                        elif three == symbols[2]:
                            count = a / b - c * d
                        elif three == symbols[3]:
                            count = a / b - c / d
                    elif two == symbols[2]:
                        if three == symbols[0]:
                            count = a / b * c + d
                        elif three == symbols[1]:
                            count = a / b * c - d
                        elif three == symbols[2]:
                            count = a / b * c * d
                        elif three == symbols[3]:
                            count = a / b * c / d
                    elif two == symbols[3]:
                        if three == symbols[0]:
                            count = a / b / c + d
                        elif three == symbols[1]:
                            count = a / b / c - d
                        elif three == symbols[2]:
                            count = a / b / c * d
                        elif three == symbols[3]:
                            count = a / b / c / d
                    #
                    # 
                    # 
                    # 
                         
    if count == 24:
        answer += "%s %s %s %s %s %s %s = %s\n"%(a,one,b,two,c,three,d,count)
        update.message.reply_text(answer)
    elif count == False:
        answer += "Impossible combination!\n"
        update.message.reply_text(answer)   

def add_handler(dp:Dispatcher):
    blackjack_handler = CommandHandler('pd24', bot)
    dp.add_handler(blackjack_handler)
             