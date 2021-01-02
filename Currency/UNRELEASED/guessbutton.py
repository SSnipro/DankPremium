from telegram.ext import Dispatcher,CommandHandler,CallbackQueryHandler
from telegram import InlineKeyboardMarkup,InlineKeyboardButton
from datetime import datetime,timedelta
import random

smallButton = InlineKeyboardButton('🔽',callback_data='b1:small')
bigButton = InlineKeyboardButton('🔼',callback_data='b1:big')

sumButton = InlineKeyboardButton('结算 🧮',callback_data='b1:sum')

gamekb = InlineKeyboardMarkup([[bigButton,smallButton,sumButton]])

joinButton = InlineKeyboardButton('加入',callback_data='b1:join')
startButton = InlineKeyboardButton('开始',callback_data='b1:start')

startkb = InlineKeyboardMarkup([[joinButton,startButton]])

# 计时器
gametime = datetime.now()
gametime2= datetime.now()

# { first_name:d, first_name:x} 
# { uid:{h:"",{first_name:d}} }
games = {}
timer = 0

def check_chatid(chatid):
    if not chatid in games.keys():
        games[chatid]={
            "h":"",
            "p":{}
            }

def getHist(chatid):
    return games[chatid]['h']

def setHist(chatid,res):
    h = games[chatid]['h']
    if len(h) > 10:
        h = h[:9] + res
    else:
        h += res
    games[chatid]['h'] = h

def getNumber():
    endNumber = 0
    msg = "数字： "
    for _i in range(3):
        rnumber = random.randint(1,6)
        endNumber += rnumber
        msg += "%s + "%rnumber
    msg = "%s= %s\n\n" % (msg[:-2],endNumber)
    return [endNumber,msg]

def sumGame(chatid):
    number,msg = getNumber()
    game = '🔽'
    if number >= 11:
        game = '🔼'
    for u in games[chatid].keys():
        if games[chatid][u] == '':
            games[chatid][u] = '没选'
        elif games[chatid][u] == game:
            games[chatid][u] = ' ✅'
        else:
            games[chatid][u] = ' ❌'
    msg += getUsers(chatid)
    return msg 

def getUsers(chatid):
    msg = ""
    for u in games[chatid].keys():
        msg += "%s:%s\n"%(u,games[chatid][u])
    return msg

def guess(update, context):
    global gametime
    chatid = update.effective_chat.id
    if not (chatid in games.keys()):
        games[chatid] = {}  
    update.message.reply_text("请选择大或小",reply_markup=startkb)
    gametime = datetime.now() + timedelta(seconds=5)

def buttonCallback(update, context):
    global games,gametime,gametime2
    query = update.callback_query 
    chatid = update.effective_chat.id
    if not (chatid in games.keys()):
        games[chatid] = {}  
    print(games)
    if query.data == 'b1:join':
        query.answer("加入游戏")
        games[chatid][update.effective_user.first_name] = ""
        query.edit_message_text(getUsers(chatid),reply_markup=startkb)
        return
    if not update.effective_user.first_name in games[chatid].keys():
        query.answer("大笨蛋%s，这不是你的游戏，别乱点！"%update.effective_user.first_name,show_alert=True)
        return
    

    if query.data == 'b1:start':
        t = datetime.now() 
        if t >= gametime:
            query.edit_message_text(getUsers(chatid),reply_markup=gamekb)
            gametime2 = datetime.now() + timedelta(seconds=5)
        else:
            query.answer("等下，别急，至少要等五秒给别人一点机会嘛",show_alert=True)
    elif query.data == 'b1:big':
        query.answer("你选择了大")
        games[chatid][update.effective_user.first_name] = "🔼"
        query.edit_message_text(getUsers(chatid),reply_markup=gamekb)
    elif query.data == 'small':
        query.answer("你选择了小")
        games[chatid][update.effective_user.first_name] = "🔽"
        query.edit_message_text(getUsers(chatid),reply_markup=gamekb)
    elif query.data == 'b1:sum':
        t = datetime.now() 
        if t >= gametime2:
            query.answer("结算开始")
            query.edit_message_text(sumGame(chatid))
            games[chatid] = {}
        else:
            query.answer("等下，别急，至少要等五秒给别人一点机会嘛",show_alert=True)



def add_handler(dp:Dispatcher):
    guess_handler = CommandHandler('PDGuessB2', guess)
    dp.add_handler(guess_handler)
    dp.add_handler(CallbackQueryHandler(buttonCallback,pattern="^b1:[A-Za-z0-9_]*"))
