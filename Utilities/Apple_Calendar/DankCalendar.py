from icalevents.icalevents import events
from telegram.ext import Dispatcher,CommandHandler,CallbackQueryHandler, CallbackContext
from datetime import date, timedelta, datetime, time
from telegram import BotCommand
import pytz
from Utilities.Apple_Calendar import setCalendar

def timer_Callback(context: CallbackContext):
    chatid = context.job.context
    tmr = date.today() + timedelta(days=1)
    print(setCalendar.cs)
    url = setCalendar.cs[str(chatid)]['url']
    es = events(url, fix_apple=True,start=tmr,end=tmr)
    msg = "~~~~~~~~~~~\n\n"
    for e in es:
        msg += f"✨{e.summary}:\n{e.description}✨\n\n🌕 Start: {e.start} \n🌑 End: {e.end}\n\n~~~~~~~~~~~\n\n"
    if es == []:
        msg = "You have no events tommorow."
    context.bot.send_message(chat_id=context.job.context, text=msg)

def cal(update,context):
    chatid = update.effective_chat.id
    context.job_queue.run_once(timer_Callback,0,context=chatid)

def run_repeating(job_queue):
    for i in range(0,len(list(setCalendar.cs))):
        chatid = list(setCalendar.cs)[i]
        j = job_queue.run_daily(timer_Callback,
                time(hour=setCalendar.cs[chatid]['hours'],minute=setCalendar.cs[chatid]['minutes'],tzinfo=pytz.timezone(setCalendar.cs[chatid]['tz'])),
                context=chatid,name=chatid)

    print('Running Fine!')

def add_handler(dp:Dispatcher):
    arctic_handler = CommandHandler('PDCal', cal)
    dp.add_handler(arctic_handler)