import random
from telegram.ext import Dispatcher,CommandHandler
from telegram import BotCommand
from Currency import bal

codes = {}

def usecodes(update,context):
    global codes
    user = update.effective_user
    uid = str(user.id)
    if not uid in codes:
        codes = {
            uid: {
                'code': False
            }
        }
    
    if len(context.args) == 0:
        update.message.reply_text('Invaid code')
    elif context.args[0] == 'hf7327g8f32gwG' and codes[uid]['code'] == False:
        update.message.reply_text('You used a code to claim $1000000.')
        codes[uid]['code'] = True
        bal.addcoins(user,1000000)
    else:
        update.message.reply_text('Invaid code: already claimed')

def add_handler(dp:Dispatcher):
    reward_handler = CommandHandler('pdusecodes', usecodes)
    dp.add_handler(reward_handler)
