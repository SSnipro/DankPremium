import config
import random
from Utilities import util
from datetime import datetime,timedelta
from telegram.ext import Dispatcher,CommandHandler, Filters, CallbackQueryHandler
from telegram import BotCommand, Animation, InlineKeyboardButton, InlineKeyboardMarkup

#  {
#       uid:{
#           first_name: "",
#           count:0,
#           coins:0
#       }
#   }
bal = config.CONFIG['bal']

def check(user):
    uid = str(user.id)
    fname = user.first_name
    if not uid in bal:
        bal[uid] = {}
        bal[uid]['fname'] = fname
        bal[uid]['coins'] = 0
        bal[uid]['count'] = 0
        bal[uid]['codes'] = {
            'code': False
        }
        bal[uid]['dailytime'] = datetime.now().strftime('%Y/%m/%d %H:%M:%S')
        bal[uid]['inv'] = {
            'perks': {
                'admin': "- Non ❌ Admin",
                'goldpass': "- ❌ Gold Pass",
                'custompass': "- ❌ Custom Pass"
            },
            'weapons': {
                'crossbow': "- ❌ Crossbow",
                'arrow': 0
            },
            'items': {
                'spaceticket': "- 🎫 Space Ticket -- [INACTIVE]" 
            },
        }
        bal[uid]['stats'] = {
            'rolename': "",
            'types': [],
            'moves': {
                '1':{
                    'name':"",
                    'type':"",
                    'power':"",
                    'acc':0,
                    'heal':0
                },
                '2':{
                    'name':"",
                    'type':"",
                    'power':"",
                    'acc':0,
                    'heal':0
                },
                '3':{
                    'name':"",
                    'type':"",
                    'power':"",
                    'acc':0,
                    'heal':0
                },
                '4':{
                    'name':"",
                    'type':"",
                    'power':"",
                    'acc':0,
                    'heal':0
                },
                '5':{
                    'name':"",
                    'type':"",
                    'power':"",
                    'acc':0,
                    'heal':0
                },
                '6':{
                    'name':"",
                    'type':"",
                    'power':"",
                    'acc':0,
                    'heal':0
                },
                '7':{
                    'name':"",
                    'type':"",
                    'power':"",
                    'acc':0,
                    'heal':0
                },
                '8':{
                    'name':"",
                    'type':"",
                    'power':"",
                    'acc':0,
                    'heal':0
                }
            },
            'atk': {
                'max': 50,
                'current': 50
            },
            'hp': {
                'max': 50,
                'current': 50
            },
            'defence': {
                'max': 50,
                'current': 50
            },
            'speed': {
                'max': 50,
                'current': 50
            }
        }

def get_count(user):
    uid = str(user.id)
    return bal[uid]['count']

def get_coins(user):
    uid = str(user.id)
    return bal[uid]['coins']

def get_arrows(user): 
    uid = str(user.id)
    return bal[uid]['inv']['weapons']['arrow']

def balence(update, context):
    user = update.message.from_user
    check(user)
#     update.message.reply_text("""🏦 ✨%s (银行ID: %s) 的银行账户余额：$%s ✨, %s 次取钱
# """%(user.first_name,user.id,get_coins(user),get_count(user)))
# coins_file = Path("/Users/Snipro/work/DankPremium/images/dino.gif")
    update.message.reply_text("🏦 ✨%s (银行ID: %s) 的银行账户余额：$%s ✨, %s 次取钱"%(user.first_name,user.id,get_coins(user),get_count(user)))

def addcoins(user,coins):
    uid = str(user.id)
    fname = user.first_name
    check(user)
    bal[uid]['coins'] += coins
    bal[uid]['count'] += 1
    bal[uid]['fname'] = fname
    bal[uid]['dailytime'] = datetime.now().strftime('%Y/%m/%d %H:%M:%S')
    config.CONFIG['bal'] = bal 
    config.save_config()

def additem(user,t,r):
    check(user)
    uid = str(user.id)
    bal[uid]['inv']['items'][r] = t
    config.CONFIG['bal'] = bal 
    config.save_config()

def addarrows(user,t):
    check(user)
    uid = str(user.id)
    bal[uid]['inv']['weapons']['arrow'] += t
    config.CONFIG['bal'] = bal 
    config.save_config()

def addweapon(user,t,r):
    check(user)
    uid = str(user.id)
    bal[uid]['inv']['weapons'][r] = t
    config.CONFIG['bal'] = bal 
    config.save_config()

def addperks(user,t,r):
    check(user)
    uid = str(user.id)
    bal[uid]['inv']['perks'][r] = t
    config.CONFIG['bal'] = bal 
    config.save_config()

def get_dailytime(uid):
    return datetime.strptime(bal[uid]['dailytime'],'%Y/%m/%d %H:%M:%S')

def set_dailytime(uid,time):
    bal[uid]['dailytime']=time.strftime('%Y/%m/%d %H:%M:%S')

def daily(update,context):
    user = update.effective_user
    check(user)
    uid = str(user.id)
    username = user.username
    if datetime.now() > get_dailytime(uid):
        c = random.randint(1000,5000)
        addcoins(user,c)
        set_dailytime(uid,datetime.now() + timedelta(days=1))
        config.save_config()
        update.message.reply_text(f'Here is your ${c} daily reward @{username}!')
    else:
        update.message.reply_text("one day didn't pass yet dummy")

def inv(update,context):
    user = update.effective_user
    uid = str(user.id)
    check(user)    
    if bal[uid]['inv']['items'] == {} and bal[uid]['inv']['weapons'] == {}  and bal[uid]['inv']['perks'] == {}:
        update.message.reply_text("You have nothing in your inventory.")
    else:
        update.message.reply_text(f"""👜 ✨{bal[uid]['fname']}'s Inventory 
        
        
🏦 Bank ID: {uid}

=-=-=-=-=-=-=-=-=-=-=-=-=-=    
    
💰 Coins: ${bal[uid]['coins']} ✨

=-=-=-=-=-=-=-=-=-=-=-=-=-=

⭐️ Perks: 

{bal[uid]['inv']['perks']['admin']}
{bal[uid]['inv']['perks']['custompass']}
{bal[uid]['inv']['perks']['goldpass']}

=-=-=-=-=-=-=-=-=-=-=-=-=-=

🧸 Items: 

{bal[uid]['inv']['items']['spaceticket']}

=-=-=-=-=-=-=-=-=-=-=-=-=-=

⚔️ Weapons: 

{bal[uid]['inv']['weapons']['crossbow']} (x{bal[uid]['inv']['weapons']['arrow']} Arrows)

=-=-=-=-=-=-=-=-=-=-=-=-=-=
    """)
        

def usecodes(update,context):
    user = update.effective_user
    uid = str(user.id)
    check(user)
    if len(context.args) == 0:
        update.message.reply_text('Invaid code')
    elif context.args[0] == 'hf7327g8f32gwG' and bal[uid]['codes']['code'] == False:
        update.message.reply_text('You used a code to claim $1000000.')
        bal[uid]['codes']['code'] = True
        addcoins(user,1000000)
    else:
        update.message.reply_text('Invaid code: already claimed')

def stats(update,context):
    user = update.effective_user
    uid = str(user.id)
    fname = user.first_name
    if bal[uid]['stats']['atk']['max'] == 50 and bal[uid]['stats']['defence']['max'] == 50 and bal[uid]['stats']['speed']['max'] == 50:
        kbs = [{
            '🦾 The Tank':'st:tank',
            '🗡 The Warrior':'st:warrior'},{
            '⚡️ The Flash':'st:flash',
            '💎 The Thief':'st:thief'
        }]
        kb = util.getkb(kbs)
        msg = f"""Choose your role! 
    
(Note: Once you've picked your role, you can only change it one more time, pick carefully!)
    
🦾 The Tank

💥 Attack: 50
🛡 Defence: 150
♥️ HP: 125
⚡️ Speed: 25

🗡 The Warrior

💥 Attack: 90
🛡 Defence: 90
♥️ HP: 95
⚡️ Speed: 85

⚡️ The Flash

💥 Attack: 130
🛡 Defence: 30
♥️ HP: 30
⚡️ Speed: 160

💎 The Thief

💥 Attack: 140
🛡 Defence: 70
♥️ HP: 50
⚡️ Speed: 120


     """
        update.message.reply_text(msg,reply_markup=kb)
    else:
        msg2 = "\n\n"
        for i in bal[uid]['stats']['types']:
            msg2 += f"{i}\n"

        msg = f"""{fname}'s stats:

{bal[uid]['stats']['rolename']}

Types: {msg2}

Status:

💥 Attack: {bal[uid]['stats']['atk']['current']} / {bal[uid]['stats']['atk']['max']}
🛡 Defence: {bal[uid]['stats']['defence']['current']} / {bal[uid]['stats']['defence']['max']}
♥️ HP: {bal[uid]['stats']['hp']['current']} / {bal[uid]['stats']['hp']['max']}
⚡️ Speed: {bal[uid]['stats']['speed']['current']} / {bal[uid]['stats']['speed']['max']}
    """
        update.message.reply_text(msg)
    
def moves(update,context):
    msg = f"-----------------"
    chatid = update.effective_chat.id
    m = ["1","2","3","4","5","6","7","8"]
    uid = str(update.effective_user.id)
    moves = bal[uid]['stats']['moves']
    for i in m:
        b = "No Healing Power"
        if not moves[i]['heal'] == 0:
            b = f"Healing Power: {bal[uid]['stats']['moves'][i]['heal']}"
        msg += f"\n\n{moves[i]['name']}\n\n{moves[i]['type']}\nPower: {moves[i]['power']} \nAccuracy: {moves[i]['acc']} \n{b}\n\n-----------------"
    context.bot.send_message(chatid, text=msg)
    
def buttonCallback(update,context):
    chatid = update.effective_chat.id
    user = update.effective_user
    uid = str(user.id)
    query = update.callback_query 
    if query.data == 'st:tank':
        query.answer("Sucess! You are now a tank.")
        bal[uid]['stats']['rolename'] = "🦾 The Tank"
        bal[uid]['stats']['types'] = []
        bal[uid]['stats']['types'].append('⚙️ Steel')
        bal[uid]['stats']['types'].append('🧱 Ground')
        bal[uid]['stats']['atk']['current'] = 50
        bal[uid]['stats']['atk']['max'] = 50
        bal[uid]['stats']['defence']['current'] = 150
        bal[uid]['stats']['defence']['max'] = 150
        bal[uid]['stats']['hp']['current'] = 125
        bal[uid]['stats']['hp']['max'] = 125
        bal[uid]['stats']['speed']['current'] = 25
        bal[uid]['stats']['speed']['max'] = 25
        query.edit_message( f"""{fname}'s stats:

{bal[uid]['stats']['rolename']}

Types: {msg2}

Status:

💥 Attack: {bal[uid]['stats']['atk']['current']} / {bal[uid]['stats']['atk']['max']}
🛡 Defence: {bal[uid]['stats']['defence']['current']} / {bal[uid]['stats']['defence']['max']}
♥️ HP: {bal[uid]['stats']['hp']['current']} / {bal[uid]['stats']['hp']['max']}
⚡️ Speed: {bal[uid]['stats']['speed']['current']} / {bal[uid]['stats']['speed']['max']}
    """)
    if query.data == 'st:warrior':
        query.answer("Sucess! You are now a warrior.")
        bal[uid]['stats']['rolename'] = "🗡 The Warrior"
        bal[uid]['stats']['types'] = []
        bal[uid]['stats']['types'].append('😀 Normal')
        bal[uid]['stats']['types'].append('🥊 Fighting')
        bal[uid]['stats']['atk']['current'] = 90
        bal[uid]['stats']['atk']['max'] = 90
        bal[uid]['stats']['defence']['current'] = 90
        bal[uid]['stats']['defence']['max'] = 90
        bal[uid]['stats']['hp']['current'] = 95
        bal[uid]['stats']['hp']['max'] = 95
        bal[uid]['stats']['speed']['current'] = 85
        bal[uid]['stats']['speed']['max'] = 85
        query.edit_message( f"""{fname}'s stats:

{bal[uid]['stats']['rolename']}

Types: {msg2}

Status:

💥 Attack: {bal[uid]['stats']['atk']['current']} / {bal[uid]['stats']['atk']['max']}
🛡 Defence: {bal[uid]['stats']['defence']['current']} / {bal[uid]['stats']['defence']['max']}
♥️ HP: {bal[uid]['stats']['hp']['current']} / {bal[uid]['stats']['hp']['max']}
⚡️ Speed: {bal[uid]['stats']['speed']['current']} / {bal[uid]['stats']['speed']['max']}
    """)
    if query.data == 'st:flash':
        query.answer("Sucess! You are now a flash.")
        bal[uid]['stats']['rolename'] = "⚡️ The Flash"
        bal[uid]['stats']['types'].append('⚡️ Thunder')
        bal[uid]['stats']['types'].append('💥 Psychic')
        bal[uid]['stats']['atk']['current'] = 130
        bal[uid]['stats']['atk']['max'] = 130
        bal[uid]['stats']['defence']['current'] = 30
        bal[uid]['stats']['defence']['max'] = 30
        bal[uid]['stats']['hp']['current'] = 30
        bal[uid]['stats']['hp']['max'] = 30
        bal[uid]['stats']['speed']['current'] = 160
        bal[uid]['stats']['speed']['max'] = 160
        query.edit_message( f"""{fname}'s stats:

{bal[uid]['stats']['rolename']}

Types: {msg2}

Status:

💥 Attack: {bal[uid]['stats']['atk']['current']} / {bal[uid]['stats']['atk']['max']}
🛡 Defence: {bal[uid]['stats']['defence']['current']} / {bal[uid]['stats']['defence']['max']}
♥️ HP: {bal[uid]['stats']['hp']['current']} / {bal[uid]['stats']['hp']['max']}
⚡️ Speed: {bal[uid]['stats']['speed']['current']} / {bal[uid]['stats']['speed']['max']}
    """)
    if query.data == 'st:thief':
        query.answer("Sucess! You are now a thief.")
        bal[uid]['stats']['rolename'] = "💎 The Thief"
        bal[uid]['stats']['types'].append('👻 Ghost')
        bal[uid]['stats']['types'].append('🥊 Fighting')
        bal[uid]['stats']['atk']['current'] = 140
        bal[uid]['stats']['atk']['max'] = 140
        bal[uid]['stats']['defence']['current'] = 70
        bal[uid]['stats']['defence']['max'] = 70
        bal[uid]['stats']['hp']['current'] = 50
        bal[uid]['stats']['hp']['max'] = 50
        bal[uid]['stats']['speed']['current'] = 120
        bal[uid]['stats']['speed']['max'] = 120
        query.edit_message( f"""{fname}'s stats:

{bal[uid]['stats']['rolename']}

Types: {msg2}

Status:

💥 Attack: {bal[uid]['stats']['atk']['current']} / {bal[uid]['stats']['atk']['max']}
🛡 Defence: {bal[uid]['stats']['defence']['current']} / {bal[uid]['stats']['defence']['max']}
♥️ HP: {bal[uid]['stats']['hp']['current']} / {bal[uid]['stats']['hp']['max']}
⚡️ Speed: {bal[uid]['stats']['speed']['current']} / {bal[uid]['stats']['speed']['max']}""")
    config.save_config()

def add_handler(dp:Dispatcher):
    dp.add_handler(CommandHandler('PDBal', balence))
    dp.add_handler(CommandHandler('PDDaily', daily))
    dp.add_handler(CommandHandler('PDInv', inv))
    dp.add_handler(CommandHandler('PDUseCodes', usecodes))
    dp.add_handler(CommandHandler('PDStats', stats))
    dp.add_handler(CommandHandler('PDMoves', moves))
    dp.add_handler(CallbackQueryHandler(buttonCallback,pattern="^st:[A-Za-z0-9_]*"))

def get_command():
    return [BotCommand('pdbal','Check your bank account!'),('pddaily','Claim your daily coins!'),('pddaily','Collect your daily coins!'),('pdinv','Check your current inventory!')]