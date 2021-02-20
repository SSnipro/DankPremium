from telegram.ext import MessageHandler, CallbackQueryHandler, Filters, Dispatcher,CommandHandler
from telegram import Message, Update, InlineKeyboardMarkup,InlineKeyboardButton
from Utilities import util

uservote = {}

def message(update,context):
    Keyboard = [{
        'Love it! ❤️ 0':'m:❤️:0',
        'Alright! 👌🏼 0':'m:👌🏼:0',
        'No. 🙅‍♂️ 0':'m:🙅‍♂️:0'
    }]
    DisplayKeyboard = util.getkb(Keyboard)
    if update.effective_chat.type == 'channel':
        chatid = update.channel_post.sender_chat.id
        msg = context.bot.edit_message_reply_markup(
            chatid, 
            update.channel_post.message_id, 
            update.channel_post.text + " ",
            reply_markup = DisplayKeyboard
            )

def add_user_vote(mid,uid):
    if not mid in uservote :
        uservote[mid] = []
    if not uid in uservote[mid] :
        uservote[mid].append(uid)
    uservote[mid].remove(uid)
    uservote[mid].append(uid)
    

def reaction_callback(update,context):
    query = update.callback_query
    cmd = query.data.split(":") # ['vote','👍']
    buttons = query.message.reply_markup.inline_keyboard
    count = int(cmd[2]) + 1
    query.answer("Voting Sucessful")
    if cmd[1] == '❤️':
        buttons[0][0] = InlineKeyboardButton(f"Love it! ❤️ {count}",callback_data=f"vote:❤️:{count}")
        query.edit_message_reply_markup(InlineKeyboardMarkup(buttons))
    elif cmd[1] == "👌🏼":
        buttons[0][1] = InlineKeyboardButton(f"Alright! 👌🏼 {count}",callback_data=f"vote:👌🏼:{count}")
        query.edit_message_reply_markup(InlineKeyboardMarkup(buttons))
    elif cmd[1] == "🙅‍♂️":
        buttons[0][2] = InlineKeyboardButton(f"No. 🙅‍♂️ {count}",callback_data=f"vote:🙅‍♂️:{count}")
        query.edit_message_reply_markup(InlineKeyboardMarkup(buttons))

def add_handler(dp:Dispatcher):
    dp.add_handler(MessageHandler(Filters.text & (~Filters.command),message))
    dp.add_handler(CallbackQueryHandler(reaction_callback,pattern="^m:[A-Za-z0-9_:]*"))
