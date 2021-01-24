import config
import pytz
from pytz import all_timezones
from telegram.ext import Dispatcher,CommandHandler, Filters

cs = config.CONFIG['cs']

def calhelp(update,context):
    chatid = str(update.effective_chat.id)
    group = str(update.effective_chat.type)
    if group == 'supergroup' or group == 'group' or group == 'channel':
        groupname = update.effective_chat.title
    elif group == 'private':
        groupname = update.effective_chat.first_name
    if not chatid in cs:
        cs[chatid] = {}
        cs[chatid]['url'] = ''
        cs[chatid]['hours'] = 0
        cs[chatid]['minutes'] = 0
        cs[chatid]['tz'] = ''
        cs[chatid]['title'] = ''
    if len(context.args) == 3:
        url = str(context.args[0])
        time = context.args[1]
        timezone = context.args[2]
        if timezone in pytz.all_timezones:
            cs[chatid]['tz'] = timezone
            update.message.reply_text('Success!')
        else:
            msg = ''
            update.message.reply_text(f'Invaid timezone.\n\nHere is a link of a list of all the timezones:\n\n✨https://gist.github.com/heyalexej/8bf688fd67d7199be4a1682b3eec7568#file-pytz-time-zones-py')
            
        print(url,time,chatid)
        cs[chatid]['url'] = url
        cs[chatid]['hours'] = int(time.split(':')[0])
        cs[chatid]['title'] = groupname
        if int(time.split(':')[1]) < 10:
            minutes = time.split(':')[1][1:]
            cs[chatid]['minutes'] = int(minutes)
        else:
            cs[chatid]['minutes'] = int(time.split(':')[1])
        config.save_config()
    else:
        update.message.reply_text('䷦ Structure: \n\n/pdsetcal@dankpbot [Your Apple Calendar URL Here] [The Time You Want The Notification Sent, For Example, 17:00] [Your Time Zone]')

def view_cal(update,context):
    chatid = str(update.effective_chat.id)
    b = ''
    msg = ''
    for i in list(cs):
        if cs[i]['minutes'] < 10:
            b = f"0{cs[i]['minutes']}"
        else:
            b = cs[i]['minutes']
        msg += f"✨ {cs[i]['title']}\n📆 Calendar URL: {cs[i]['url']}\n🔔 Notification Time: {cs[i]['hours']}:{b}\n\n"
    update.message.reply_text(msg)

def add_handler(dp:Dispatcher):
    dp.add_handler(CommandHandler('PDSetCal', calhelp))
    dp.add_handler(CommandHandler('PDViewCal', view_cal))