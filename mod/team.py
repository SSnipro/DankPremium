import random

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

def check_team(uid,chatid,team):
    if not chatid in teams:
        teams[chatid] = {}

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
