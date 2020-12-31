
# def get_dailytime(chatid,uid):
#     return datetime.strptime(coins[chatid][uid]['dailytime'],'%Y/%m/%d %H:%M:%S')

# def set_dailytime(chatid,uid,time):
#     coins[chatid][uid]['dailytime']=time.strftime('%Y/%m/%d %H:%M:%S')

# def daily(chatid,user):
#     chatid = str(chatid)
#     check_user(chatid,user)
#     uid = str(user.id)
#     if datetime.now() > get_dailytime(chatid,uid):
#         c = random.randint(1,100)
#         coins[chatid][uid]['coins'] += c
#         set_dailytime(chatid,uid,datetime.now() + timedelta(minutes=5))
#         save()
#         return c
#     else:
#         return 0