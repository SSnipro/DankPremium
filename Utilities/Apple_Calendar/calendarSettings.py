import config
from telegram.ext import Dispatcher,CommandHandler, Filters

cs = {}

def calhelp(update,context):
    chatid = update.effective_chat.id
    if not chatid in cs:
        cs[chatid] = {
            'url':'',
            'hours':0,
            'minutes':0
        }
    if len(context.args) == 2:
        update.message.reply_text('Success!')
        url = str(context.args[0])
        time = context.args[1]
        print(url,time,chatid)
        cs[chatid]['url'] = url
        cs[chatid]['hours'] = int(time.split(':')[0])
        if time.split(':')[1] == "00":
            minutes = 0
            cs[chatid]['minutes'] = minutes
        else:
            cs[chatid]['minutes'] = int(time.split(':')[1])
        config.CONFIG['cs'] = cs 
        config.save_config()
    else:
        update.message.reply_text('Structure: \n\n/pdsetcal@dankpbot [Your Apple Calendar URL Here] [The Time You Want The Notification Sent, For Example, 17:00])

def add_handler(dp:Dispatcher):
    dp.add_handler(CommandHandler('PDSetCal', calhelp))