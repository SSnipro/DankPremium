from telegram.ext import CommandHandler, Dispatcher, CallbackQueryHandler
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, BotCommand
from datetime import datetime,timedelta
import random
from Currency import bal
from Utilities import team,place,util


# 文档
# 
# 伪代码
# 

# 数据结构

# 操作数据的函数

# 功能


search = {}

#/pdsearch
#  bot   1 to 1 game
#   1 to group

#  每天 第一个人 /search  bot 公布，在 xxx 有神秘大奖 
#  组成一个队伍 一起去找   一起找增加找到的概率  1 ->  random[100:1]     人多了  [100:n]
#  某个小时找到的概率变高  [50:n]
#  怪物[hp,atk,def,speed]     小队[hps,atks,defs,speeds] -> 奖励或输  [地方]  [怪物]  [宝物]
#  [地方]  {高级，普通，初级}   怪物等级
 
#  1. 
#  老房东你想搜索哪里
#Where do you want to search? [ air, bank, attic, 加入搜索 ]  -> sendmessage noah 搜索 air的msg

#  2. air
#  老房东去air......
#  search结果 $   * 3  + bal
#  [再次搜索-> 1 | 帮助搜索(3) ]   if click 再次搜索的人 不是 /pdsearch  -> sendmessage 

# noah 你想搜索哪里
# 

#attic
    

def searching(update, context):
    # Search = [
    #     "You searched the air and found some new unknown elements. You gained $300. \n\n你在空气里找到了一些新元素。你得到了 $300。",
    #     "YOU ROBBED THE BANK AND GAINED $120. NOW RUN \n\n你抢劫了银行并得到了 $120。快跑!!!!!", 
    #     "You tried to rob the bank and got shot. Might need to learn how to play dodgeball next time. \n\n你尝试去抢劫银行却被警察击中。下次练完躲避球再来吧。", 
    #     "You begged on the street and got mistaken for a hobo. Did you forget that they don't give $ to beggers anymore? \n\n你在路上讨钱。你忘了他们不再给讨钱的人 $ 了么？", 
    #     "You searched the school and got mistaken for a kidnapper. You got jailed. \n\n你搜索了学校但被误以为一个拐卖小孩的骗子。你入狱了。", 
    #     "You searched the hospital, not konwing that it's a great mistake. You got COVID-19 and died. \n\n你搜索了医院，但被流感传染。你挂了。", 
    #     "You searched the hospital and found a doctor's bag. You found a wallet with $20 inside. \n\n你搜索了医院并找到了一名医生的包。你获得了 $20。", 
    #     "You found $40 in the attic. How long had it been here? \n\n你在阁楼找到了 $40。在这里待了多久了？", 
    #     "You searched the haunted house and found a vault. You opened it and found $1000! Luckily there was no ghosts inside \n\n你搜索了鬼屋并找到了一个金库。你打开了它并找到了 $1000！幸好里面没有鬼。", 
    #     "You searched a tree and found buried treasure worth $270. GG! \n\n你搜索了一棵树并找到了一批宝藏。你得到了 $270。 酷！", 
    #     "You searched L - Park, not knowing it's a park for losers. Anyway, at least you got $9 from a bet with another kid. \n\n你搜索了 L - 公园，最终收获了 $9。", 
    #     "You searched the haunted house and got murdered by a ghost. RIP. \n\n你尝试去搜索鬼屋。 你被 幽灵 给击败了。"
    #     ]
    # msg4 = random.choice(Search)
    # user = update.message.from_user.first_name
    # if msg4 == Search[0]:
    #     bal.addcoins(user,300)
    # elif msg4 == Search[1]:
    #     bal.addcoins(user,120)
    # elif msg4 == Search[6]:
    #     bal.addcoins(user,20)
    # elif msg4 == Search[7]:
    #     bal.addcoins(user,40)
    # elif msg4 == Search[8]:
    #     bal.addcoins(user,1000)
    # elif msg4 == Search[9]:
    #     bal.addcoins(user,270)
    # elif msg4 == Search[10]:
    #     bal.addcoins(user,9)
    # msg4 += "\n\nAuthorised By Noah <3\n作者：Noah"

    dest = place.random_destination()

    gameskb = [{
            dest[0].name:f'sr:p:{dest[0].name}'},{
            dest[1].name:f'sr:p:{dest[1].name}'},{
            dest[2].name:f'sr:p:{dest[2].name}'
        }]

    gamekb = util.getkb(gameskb)

    update.message.reply_text(f'Where do you want to search? {dest[0].name}, {dest[1].name} or {dest[2].name}?',reply_markup=gamekb)

def buttonCallback(update,context):
    chatid = update.effective_chat.id
    user = update.effective_user
    uid = user.id
    # query.data     
    # sr:p:....    列出来的是places
    # sr:f:....    列出来的是打斗结果
    query = update.callback_query 
    action = query.data.split(':')[1]
    restartkb = [{
        'Search Again':'sr:f:sa'
    }]

    fightkb = [{
        'Fight!':'sr:p:f',
        'Run!':'sr:f:run'
    }]

    dest = place.random_destination()

    gameskb = [{
                dest[0].name:f'sr:p:{dest[0].name}'},{
                dest[1].name:f'sr:p:{dest[1].name}'},{
                dest[2].name:f'sr:p:{dest[2].name}'
            }]

    if action == 'p':
        placename = query.data.split(':')[2]
        p = place.Place(placename)
        if placename == 'f':
            query.edit_message_text(f"You searched the {p.name} and found...\n\n🥊 BOSS FIGHT!\n\nIt's {p.boss.name} !\n\n♥️ HP: {p.boss.hp}\n⚔️ Attack: {p.boss.atk}\n🛡 Defence: {p.boss.defence}\n⚡️ Speed: {p.boss.speed} \n\nWanna know what he looks like? Check out {p.boss.image}",reply_markup=util.getkb(fightkb))
            # if team.teams[chatid][team] == {}:
            #     team.create_team(uid,chatid,random.randint(1,100))
            # if team.members[chatid][uid]['spd'] >= p.boss.speed:
            #     msg = f'You won the fight!\n\nYou searched the {p.name} and found ${p.coins}! Search again?'
            #     bal.addcoins(user,p.coins)
            # else: 
            #     msg = 'die'
            msg = f'You won the fight!\n\nYou searched the {p.name} and found ${p.coins}! Search again?'
            query.edit_message_text(msg,reply_markup=util.getkb(gameskb))
        # 选择place
        else:
            if p.boss == []:
                query.edit_message_text(f'You searched the {p.name} and found ${p.coins}',reply_markup=util.getkb(restartkb) )
                bal.addcoins(user,p.coins)
    elif action == "f":
        msg = ""
        if query.data.split(':')[2] == "run":
            msg = "You ran away! Search again?"
        elif query.data.split(':')[2] == "sa":
            msg = f'Where do you want to search? {dest[0].name}, {dest[1].name} or {dest[2].name}?'
        query.edit_message_text(msg,reply_markup=util.getkb(gameskb))
        


def add_handler(dp:Dispatcher):
    search_handler = CommandHandler('PDSearch', searching)
    dp.add_handler(search_handler)
    dp.add_handler(CallbackQueryHandler(buttonCallback,pattern="^sr:[A-Za-z0-9_]*"))




