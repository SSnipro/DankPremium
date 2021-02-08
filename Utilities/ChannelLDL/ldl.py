from telegram.ext import MessageHandler, CallbackQueryHandler, Filters, Dispatcher,CommandHandler
from telegram import Message, Update, InlineKeyboardMarkup,InlineKeyboardButton
from Utilities import util

uservote = {}

def message(update,context):
    kb = [{
        'Love it! ❤️ 0':'m:❤️:0',
        'Alright! 👌🏼 0':'m:👌🏼:0',
        'No. 🙅‍♂️ 0':'m:🙅‍♂️:0'
    }]
    ckb = util.getkb(kb)
    if update.effective_chat.type == 'channel':
        chatid = update.channel_post.sender_chat.id
        msg = context.bot.edit_message_reply_markup(chatid, update.channel_post.message_id, update.channel_post.text+" ",reply_markup=ckb)

def add_user_vote(mid,uid,new):
    if not mid in uservote :
        uservote[mid] = {}
    if not uid in uservote[mid] :
        uservote[mid][uid] = ""
    uservote[mid][uid] = str(new)
    print(uservote)

def buttonCallback(update,context):
    msg = "Voting Results:\n\n"
    query = update.callback_query
    mid = query.message.message_id
    cmd = query.data.split(":") 
    user = update.effective_user
    first_name = user.first_name
    uid = user.id
    chatid = update.channel_post.sender_chat.id
    buttons = query.message.reply_markup.inline_keyboard
    count = int(cmd[2]) + 1
    query.answer("Voting Successful!")
    if cmd[1] == '❤️':
        add_user_vote(mid,uid,'❤️')
        buttons[0][0] = InlineKeyboardButton(f"Love it! ❤️ {count}",callback_data=f"m:❤️:{count}")
        query.edit_message_reply_markup(InlineKeyboardMarkup(buttons))
        if uservote[mid] == {}:
            context.bot.send_message(msg)
        else: 
            context.bot.edit_message_text(chatid,update.channel_post.message_id,update.channel_post.text+f"{first_name} voted {uservote[mid][uid]}")
    elif cmd[1] == "👌🏼":
        add_user_vote(mid,uid,'👌🏼')
        buttons[0][1] = InlineKeyboardButton(f"Alright! 👌🏼 {count}",callback_data=f"vote:👌🏼:{count}")
        query.edit_message_reply_markup(InlineKeyboardMarkup(buttons))
        if uservote[mid] == {}:
            context.bot.send_message(msg)
        else: 
            context.bot.edit_message_text(chatid,update.channel_post.message_id,update.channel_post.text+f"{first_name} voted {uservote[mid][uid]}")
    elif cmd[1] == "🙅‍♂️":
        add_user_vote(mid,uid,'🙅‍♂️')
        buttons[0][2] = InlineKeyboardButton(f"No. 🙅‍♂️ {count}",callback_data=f"vote:🙅‍♂️:{count}")
        query.edit_message_reply_markup(InlineKeyboardMarkup(buttons))
        if uservote[mid] == {}:
            context.bot.send_message(msg)
        else: 
            context.bot.edit_message_text(chatid,update.channel_post.message_id,update.channel_post.text+f"{first_name} voted {uservote[mid][uid]}")
   
def add_handler(dp:Dispatcher):
    dp.add_handler(MessageHandler(Filters.text & (~Filters.command),message))
    dp.add_handler(CallbackQueryHandler(buttonCallback,pattern="^m:[A-Za-z0-9_]*"))
