from icalevents.icalevents import events
from telegram.ext import Dispatcher,CommandHandler,CallbackQueryHandler
from datetime import date, timedelta, datetime
from telegram import BotCommand

def cal(update,context):
    user = update.effective_user
    url = "webcal://p21-caldav.icloud.com/published/2/MTczNjk0NjYxNTE3MzY5NCI4VvgO8d5bABgiqGFi4zClDgddjpLB5E6CykOqA35uDCfggM9Tbo2CIE2TV6rNNiQaVK2OuNAwgWSOr2MBS7Q"
    es = events(url, fix_apple=True)
    # update.message.reply_text("Check")
    msg = "明天的事件："
    msg2 = ""
    msg3 = ""
    print(es)
    now = datetime.now()
    n = datetime.now() + timedelta(days=1)
    current_time = now.strftime("%Y-%m-%d %H:%M:%S")
    tmr = n.strftime("%Y-%m-%d")
    if current_time.split(' ')[1].split(':')[1] == '9':
        
    # c = current_time.split(' ')[0].split('/')
    # start = date(int(c[0]),int(c[1]),int(c[2]))
    # end = date(int(c[0]),int(c[1]),int(c[2])+1)
    for e in es: 
        et = str(e.__dict__['start'])
        et = et[:-15]
        print(f"et: {et}")
        print(f"tmr: {tmr}")
        if et == tmr:
            msg += f"{e.__dict__['summary']}: {e.__dict__['description']}\n"
        print(e)
    
    # ev = events(url=url, start=start, end=end)[0]
    # print(ev)
    
    update.message.reply_text(msg)
    # update.message.reply_text(str(current_time))

def add_handler(dp:Dispatcher):
    arctic_handler = CommandHandler('PDCal', cal)
    dp.add_handler(arctic_handler)