import random
from telegram.ext import Dispatcher,CommandHandler,CallbackQueryHandler
from telegram import InlineKeyboardMarkup,InlineKeyboardButton, BotCommand
from Currency import bal

#   /blackjack
#    
#   help 
#   user : 2
#   |要牌|停牌
# 
#   点了要牌 or 停牌
# 
#   user: 2+10=12
#   user: 1 停
#   |要牌|停牌
# 
#  所有的人都停了
#  庄: 1+3+5=9  输了!
#  user: 2+10=12 赢了！
#  user: 12      输了！
# 

hit = InlineKeyboardButton('要牌',callback_data='bj:hit')
save = InlineKeyboardButton('停牌',callback_data='bj:save')

sumButton = InlineKeyboardButton('结算 🧮',callback_data='bj:sum')
gamekb = InlineKeyboardMarkup([[hit,save,sumButton]])
gametime = 0
#  {chatid: { "DMII":[],"users":{ uid:{"name":"firstname,"cards":[1,2,3,4],state:'t' } }  } }
games = {}


def check_chatid(chatid):
    global games
    if not chatid in games.keys():
        games[chatid]={
            "DMII":{'cards':[],'state':"🔴 停牌"},
            "users":{}
            }

def getCard(chatid,uid,first_name):
    global games    
    check_chatid(chatid)
    if not uid in games[chatid]['users'].keys():
        games[chatid]['users'][uid] = {}
        games[chatid]['users'][uid]["name"]=first_name
        games[chatid]['users'][uid]["cards"]=[]
        games[chatid]['users'][uid]["state"]="🟢 要牌"
    card = random.randint(1,11)
    games[chatid]['users'][uid]["cards"].append(card)

def savee(chatid, uid, first_name):
    check_chatid(chatid)
    global games 
    games[chatid]['users'][uid]["state"]="🔴 停牌"

# def ifsaved(chatid, uid, first_name)
#     check_chatid(chatid)
#     if games[chatid]['users'][uid]["state"]="t"
#         return True
#     elif games[chatid]['users'][uid]["state"]="h"
#         return False
#     elif games[chatid]['users'][uid]["state"]=""
#         return False

def startGame(chatid,uid):
    global games
    check_chatid(chatid)
    card = random.randint(1,11)
    games[chatid]['DMII']['cards'].append(card)
    for _ in games['users'].keys():
        games[chatid]['users'][uid]['card'].append(card)

def showState(chatid):
    #  庄家: 
    # 
    #  u1: adsfadsfasdf
    #  u2: aadsfasdffda 停牌
    msg = ""
    msg += f"庄家: {games[chatid]['DMII']['cards']}"
    #  {chatid: { "DMII":[],"users":{ uid:{"name":"firstname,"cards":[1,2,3,4],state:'t' } }  } }
    for uid in games[chatid]['users'].keys():
        msg += f" {games[chatid]['users'][uid]['name']}: {games[chatid]['users'][uid]['cards']}"
        if games[chatid]['users'][uid]['state'] == '🔴 停牌':
            msg += "停牌\n"
        else:
            msg += "\n"

def bjhelp():
  return """ 
    二十一点
    """
sc = int(random.randint(5,20))
msg88888 = ""

def DMII_count(chatid):
    count = 0 
    for i in games[chatid]['DMII']['cards']:
        count += i # :)
    return count

def userCount(chatid, uid):
    counts = 0 
    for j in games[chatid]['users'][uid]["cards"]:
        counts += j # :)
    return counts

roles = ['👮🏻‍♀️','👷🏻‍♂️','💂🏻‍♂️','👨🏻‍⚕️','👨🏻‍🎓','👩🏻‍✈️','🤴🏻','👸🏻']
role = random.choice(roles)

def getUsers(chatid):
    global role
    msg = ""
    print(games[chatid])
    msg += "🤖 DMII: %s = %s %s\n\n"%(games[chatid]['DMII']['cards'],DMII_count(chatid),games[chatid]['DMII']['state'])
    for u in games[chatid]['users'].keys():
        msg += "%s %s: %s = %s %s\n"%(role,games[chatid]['users'][u]['name'],games[chatid]['users'][u]["cards"],userCount(chatid, u),games[chatid]['users'][u]['state'])
    
    return msg

def bot(update,context):
    user = update.message.from_user
    # []
    # 至少发一张
    # while count < 10 一定再发一张
    # 
    # if count < 21  > 10
    #   一半机会再发一张
    # stop
    global games
    chatid = update.effective_chat.id
    check_chatid(chatid)
    card = random.randint(1,11)
    # 至少发一张
    if len(games[chatid]['DMII']['cards']) == 0:
        games[chatid]['DMII']['cards'].append(card)
    # while count < 10 一定再发一张
    while DMII_count(chatid) < 11:
        card = random.randint(1,11)
        games[chatid]['DMII']['cards'].append(card)
    msg = ""
    if random.choice([True,False]) and DMII_count(chatid) <= 21 and DMII_count(chatid) >= 11:
        card = random.randint(1,11)
        games[chatid]['DMII']['cards'].append(card)
    msg += f"Bot: \n{games[chatid]['DMII']['cards']} total: {DMII_count(chatid)}"
    update.message.reply_text(getUsers(chatid),reply_markup=gamekb)

def ccl(chatid,user):
    bal.check(user)
    # 从games生成[[uid:count]......[dmii:count]]
    check_chatid(chatid)
    gamecount = []
    # {-1001366387264: 
    #   {'DMII': [], '
    #    users': {
    #      932729306: {'name': 'Sichengthebest', 'cards': [8, 4, 2, 9, 11, 4, 8], 'state': 'h'}, 
    #      465307161: {'name': '老房东', 'cards': [6], 'state': 'h'}, 
    #      1360440667: {'name': 'Noah', 'cards': [10], 'state': 'h'}}}}
    for u in games[chatid]['users'].keys():
        gamecount.append([u,userCount(chatid,u)])
    gamecount.append(['DMII',DMII_count(chatid)])
    # 对 [[uid:count]......[dmii:count]] 排序'
    final = sort(gamecount)
    # for aa in [a,b,dmii,c,d,e]
    #   if aa > 21 set 爆
    #   elif a <=21 and  have_win==false  赢了 set have_win=true print(f"start:{gamecount}|{final}")
    # [[465307161, 7], [1360440667, 12], ['DMII', 10]]  
    win = False
    max = 0 
    for a in final:
        uid = a[0]
        if (win and a[1] != max) or a[1] > 21:
            if not a[0] == 'DMII':
                games[chatid]['users'][uid]["state"]="❌ 失败 💥 $%s - $1000"%(bal.get_coins(user))
            else:
                games[chatid]['DMII']['state']="❌ 失败"
        else:
            if not a[0] == 'DMII':
                games[chatid]['users'][uid]["state"]="✅ 胜利 💰 $%s + $2000"%(bal.get_coins(user))
            else:
                games[chatid]['DMII']['state']="✅ 胜利"
            win = True
            max = a[1]
    
            
            
def sort(gamecount):
    final = []
    # []           [12,15,12,1]    15,1
    # [15]         [12,12,1]       12,0
    # [15,12]      [12,1]          12,0
    # [15,12,12]   [1]
    # [15,12,12,1] []
    #
    # [[465307161, 7], [1360440667, 12], ['DMII', 10]]       
    for j in range(0,len(gamecount)):
        print(j)
        value = 0
        index = 0
        for i in range(0,len(gamecount)):
            print(i)
            if gamecount[i][1] > value:
                value = gamecount[i][1]
                index = i
        final.append([gamecount[index][0],gamecount[index][1]])
        gamecount.remove([gamecount[index][0],gamecount[index][1]])
    print (final)
    # print("%s,%s"%(DMII_count(chatid),userCount(chatid, uid)))
    return final



def button(update,context):
    user = update.effective_user
    uid = update.effective_user.id
    query = update.callback_query 
    first_name = update.effective_user.first_name
    global games
    chatid = update.effective_chat.id
    check_chatid(chatid)
    if query.data == 'bj:hit':
        # 给user发牌
        check_chatid(chatid)
        getCard(chatid,uid,first_name)
        query.edit_message_text(getUsers(chatid),reply_markup=gamekb)
    elif query.data == 'bj:save':
        games[chatid]['users'][uid]['state'] = "🔴 停牌"
        query.edit_message_text(getUsers(chatid),reply_markup=gamekb)
    elif query.data == 'bj:sum':
        bal.check(user)
        ccl(chatid,user)
        if games[chatid]['users'][uid]["state"]=="❌ 失败 💥 $%s - $1000"%(bal.get_coins(user)):
            bal.addcoins(user,-1000)
        elif games[chatid]['users'][uid]["state"]=="✅ 胜利 💰 $%s + $2000"%(bal.get_coins(user)):
            bal.addcoins(user,2000)
        query.edit_message_text(getUsers(chatid))
        games = {}
        

def add_handler(dp:Dispatcher):
    blackjack_handler = CommandHandler('PDBj', bot)
    dp.add_handler(blackjack_handler)
    dp.add_handler(CallbackQueryHandler(button,pattern="^bj:[A-Za-z0-9_]*"))

def get_command():
    return [BotCommand('pdbj','Play the Blackjack Game!')]


