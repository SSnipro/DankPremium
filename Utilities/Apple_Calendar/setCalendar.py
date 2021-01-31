import config
import pytz
from pytz import all_timezones
from telegram.ext import Dispatcher,CommandHandler, Filters, Updater
from Utilities.Apple_Calendar import DankCalendar
import os
from Utilities import mysystemd

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
            update.message.reply_text(f"Success! You will receive a notification from Dank Premium in THIS CHAT everyday at {time}.")
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
        DankCalendar.run_repeating(context.job_queue)
    else:
        update.message.reply_text('䷦ Structure: \n\n/pdsetcal@dankpbot [Your Apple Calendar URL Here] [The Time You Want The Notification Sent, For Example, 17:00] [Your Time Zone]')

def view_jobs(update,context):
    chatid = update.effective_chat.id
    msg = ''
    jobs = context.job_queue.jobs()
    del jobs
    jobs = context.job_queue.jobs()
    for j in jobs:
        msg += f'{j.name} {j.next_t}\n'
    update.message.reply_text(msg)

def view_cal(update,context):
    minutes = ''
    msg = ''
    for chatid in list(cs):
        if cs[chatid]['minutes'] < 10:
            minutes = f"0{cs[i]['minutes']}"
        else:
            minutes = cs[chatid]['minutes']
        msg += f"✨ {cs[chatid]['title']}\n📆 Calendar URL: {cs[chatid]['url']}\n🔔 Notification Time: {cs[chatid]['hours']}:{minutes}\n\n"
    update.message.reply_text(msg)

def chatid(update,context):
    chatid = update.effective_chat.id
    uid = update.effective_user.id
    update.message.reply_text(f"Chatid: {chatid}, Uid: {uid}")

def add_handler(dp:Dispatcher):
    dp.add_handler(CommandHandler('getChatid', chatid))
    dp.add_handler(CommandHandler('PDSetCal', calhelp))
    dp.add_handler(CommandHandler('PDViewCal', view_cal))
    dp.add_handler(CommandHandler('PDViewJobs', view_jobs))