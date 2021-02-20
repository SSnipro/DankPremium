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

def add_user_vote(data,mid,uid,buttons):
    options = {
        "❤️" : 'Love it! ❤️ ',
        "👌🏼": 'Alright! 👌🏼 ',
        "🙅‍♂️": 'No. 🙅‍♂️ '
    }
    print(data)
    data_choice = data[1]
    data_count = int(data[2])
    print(data_count,data_choice)
    if not mid in uservote:
        uservote[mid] = {}
    if not uid in uservote[mid]:
        uservote[mid][uid] = data_choice
        data_count += 1
        buttons[data_choice][0]['text'] = f"{options[data_choice]}{data_count}"
        print(buttons[data_choice][0])
    # c = {
    #     "❤️":0,
    #     "👌🏼":1,
    #     "🙅‍♂️":2
    #     }
    # ctrans = {
    #     '❤️':'Love it! ❤️ ',
    #     '👌🏼':'Alright! 👌🏼 ',
    #     '🙅‍♂️':'No. 🙅‍♂️ '}

    # choice = c[ch]

    # count = int(buttons[choice][0].callback_data.split(":")[2])
    # print(buttons)
    # if not mid in uservote :
    #     uservote[mid] = {}
    # if not uid in uservote[mid]:
    #     uservote[mid][uid] = choice
    #     count += 1
    #     buttons[choice][0].text = f"{ctrans[ch]}{count}"
    #     buttons[choice][0].callback_data = f"m:{choice}:{count}"
    # else:
    #     if uservote[mid][uid] == choice:
    #         count -= 1
    #         buttons[choice][0].text = f"{ctrans[ch]}{count}"
    #         buttons[choice][0].callback_data = f"m:{ch}:{count}"
    #         uservote[mid].pop(uid)
    #     else:
    #         count += 1
    #         buttons[choice][0].text = f"{ctrans[ch]}{count}"
    #         buttons[choice][0].callback_data = f"m:{ch}:{count}"
    #         oc = uservote[mid][uid]
    #         ocount = int(buttons[c[o]][0].callback_data.split(":")[2])
    #         ocount -= 1
    #         buttons[c[o]][0].text = f"{ctrans[o]}{ocount}"
    #         buttons[c[o]][0].callback_data = f"m:{o}:{ocount}"
    #         uservote[mid][uid] = choice
    # return buttons

def reaction_callback(update,context):
    query = update.callback_query
    data = query.data.split(":") 
    mid = query.message.message_id
    uid = update.effective_user.id
    buttons = query.message.reply_markup.inline_keyboard

    Keyboard = add_user_vote(data,mid,uid,buttons)

    query.answer("Voting Sucessful!")
    query.edit_message_reply_markup(InlineKeyboardMarkup(Keyboard))
       
def add_handler(dp:Dispatcher):
    dp.add_handler(MessageHandler(Filters.text & (~Filters.command),message))
    dp.add_handler(CallbackQueryHandler(reaction_callback,pattern="^m:[A-Za-z0-9_:]*"))
