import random
from telegram.ext import CommandHandler, Dispatcher, CallbackQueryHandler
from Utilities import util
# teams:{
#     chatid:{
#         'team_name':{
#         'owner': Noah,
#         'member':[noah,sicheng]
#     }   
#     }
# } 
# {'001': {'@SSnipro': {'owner': 'noah', 'members': ['noah']}, 'da bug': {'owner': 'sicheng', 'members': ['sicheng', 'parker']}}}
teams = {}

# member :{
#     chatid:{
#         noah:{
#             hp: 120
#             atk: 180
#             defence: 160
#             speed: 170
#         }
#         sicheng:{
#             hp: 150
#             atk: 120
#             defence: 
#         }
#     }
# }
members = {}

def help(update,context):
    update.message.reply_text("Help")

def check_member(uid,chatid):
    if not chatid in members:
        members[chatid] = {}
    
    if not uid in members[chatid]:
        members[chatid][uid] = {}
        members[chatid][uid]['hp'] = random.randint(75,175)
        members[chatid][uid]['atk'] = random.randint(80,180)
        members[chatid][uid]['def'] = random.randint(80,180)
        members[chatid][uid]['spd'] = random.randint(75,175)

def change_hp(uid,chatid,change):
    check_member(uid,chatid)
    members[chatid][uid]['hp'] += change
    return members[chatid][uid]['hp']

def check_chat(chatid):
    if not chatid in teams:
        teams[chatid] = {}

def check_team(uid,chatid,team):
    check_chat(chatid)
    if not team in teams[chatid]:
        return False
    return True

def create_team(uid,chatid,team):
    check_member(uid,chatid)
    if check_team(uid,chatid,team) == False:
        if not chatid in teams:
            teams[chatid] = {}

        if not team in teams[chatid]:
            teams[chatid][team] = {}
            teams[chatid][team]['owner'] = uid
            teams[chatid][team]['members'] = [uid]
            return True
    return False

def join_team(uid,chatid,team):
    check_member(uid,chatid)
    if check_team(uid,chatid,team) :
        teams[chatid][team]['members'].append(uid)
        return True
    return False

def leave_team(uid,chatid,team):
    check_member(uid,chatid)
    if check_team(uid,chatid,team) :
        if uid in teams[chatid][team]['owner']:
            del teams[chatid][team]
        elif uid in teams[chatid][team]['members']:
            teams[chatid][team]['members'].remove(uid)
            return True 
    return False

# def create(update,context):
#     chatid = update.effective_chat.id
#     user = update.effective_user
#     uid = user.id
#     first_name = user.first_name
#     if len(context.args) == 0:
#         help(update,context)
#     else: 
#         message = context.args[0]
#         update.message.reply_text(f'{create_team(first_name,chatid,message)}')
#         print(teams)
#         print(chatid) 

def listTeams(update,context):
    # Noah团队：uname、uname、uname
    # 老房东团队： uname、uname、uname
    # 创建团队
    # Noah团队(uid)(2): 离开
    # 老房东团队(uid)(1): 加入入

    # text:callbackdata
    teamskb = []
    chatid = update.effective_chat.id
    user = update.effective_user
    uid = user.id
    create_button = True
    check_chat(chatid)
    for  t  in teams[chatid]:
        teamskb.append({t:f't:{t}'})
        if teams[chatid][t]['owner'] != uid: 
            create_button = False
    if create_button:
        teamskb.append({"创建新团队":"t:create"})

    msg = "None"
    for  t  in teams[chatid]:
        msg = f"""{t}:
   Owner: {teams[chatid][t]['owner']}
   Members:"""
        print(msg)
        for m in teams[chatid][t]['members']:
            msg += f" {m}\n"
    teamkb = util.getkb(teamskb)
    update.message.reply_text(msg,reply_markup=teamkb)


def buttonCallback(update,context):
    user = update.effective_user
    uid = user.id
    chatid = update.effective_chat.id
    first_name = user.first_name
    query = update.callback_query
    tn = 1
    if query.data == 't:create':
        create_team(first_name,chatid,f'Team {first_name} (银行ID: {uid}) [{tn} members]')

if __name__ == '__main__':
    print(f"check_member noah:{check_member('noah','001')}")
    print(members)
    print(f"change_hp: {change_hp('noah','001',120)}")
    print(members)
    print(f"create_team noah :{create_team('noah','001','@SSnipro')}")
    print(members)
    print(teams)
    print(f"create_team sicheng: {create_team('sicheng','001','da bug')}")
    print(members)
    print(teams)
    print(f"join_team parker to da bug :{join_team('parker','001','da bug')}")
    print(f"join_team noah to da bug :{join_team('noah','001','da bug')}")
    print(members)
    print(teams)
    print(f"leave_team noah to da bug:{leave_team('noah','001','da bug')}")
    print(members)
    print(teams)
    print(f"leave_team noah to da bug:{leave_team('noah','001','da bug')}")
    print(members)
    print(teams)
    print(f"leave_team sicheng to da bug:{leave_team('sicheng','001','da bug')}")
    print(members)
    print(teams)

def add_handler(dp:Dispatcher):
    # dp.add_handler(CommandHandler('PDCreateTeam', create))
    dp.add_handler(CommandHandler('PDListTeams', listTeams))
    dp.add_handler(CallbackQueryHandler(buttonCallback,pattern="^t:[A-Za-z0-9_]*"))