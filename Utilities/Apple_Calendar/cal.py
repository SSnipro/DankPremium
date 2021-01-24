from telegram.ext import Dispatcher,CommandHandler,CallbackQueryHandler, CallbackContext

def cal(update,context):
    update.message.reply_text("""
📆 Apple Calendar

/PDSetCal@dankpbot to set up your calendar
/PDCal@dankpbot to view your events tommorrow
/PDViewCal@dankpbot to view all the information of calendars in all groups
    """)

def add_handler(dp:Dispatcher):
    arctic_handler = CommandHandler('PDCalhelp', cal)
    dp.add_handler(arctic_handler)