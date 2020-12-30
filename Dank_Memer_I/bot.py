Fish = ["LOL You got nothing, git gud.", "You brought one common fish and gained 5 xp!", "You brought back two common fishes and gained 10 xp!", "You brought back four common fishes and gained 20 xp!", "You brought back one RARE fish and gained 100 xp! Whoo Hoo!", "You fished up a bank note and gained 700 xp. What?"]
Search = ["Air", "Bank", "Street", "School", "Hospital", "Attic", "Haunted House", "Tree", "L - Park"]
Hunt = ["LOL you suck, you found nothing to hunt", "You brought back a skunk and gained 10 xp!", "You brought back a rabbit and gained 15 xp!", "You brought back a duck and gained 25 xp!", "You brought back a boar and gained 70 xp!", "Holy Moly! You brought back a DRAGON and agained 400 xp! How'd you even manage that?"]
Beg = ["You got shot by a robber for being a spectator. Rip", "Snipro Bot Donated 50 xp to you!"]
from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters
import os
 
def start(update, context):
    print(update)
    msg = "Hi %s. You are talking in %s"%(
        update.message.from_user.first_name,
        update.message.chat.type)
    context.bot.send_message(chat_id=update.effective_chat.id,text="Sup. My Name is Snipro Bot.%s"%(msg))

def echo(update, context):
    print(update.message.from_user.first_name)
    msg2 = "%s said %s, Your user id is: %s, The language spoken is %s."%(
        update.message.from_user.first_name,
        update.message.text,
        update.message.from_user.id,
        update.message.from_user.language_code)
    context.bot.send_message(chat_id=update.effective_chat.id, text=msg2)

def read_file_as_str(file_path):
    # 判断路径文件存在
    if not os.path.isfile(file_path):
        raise TypeError(file_path + " does not exist")

    # 读取文件内容到all_the_text
    all_the_text = open(file_path).read()
    # print type(all_the_text)
    return all_the_text

TOKEN=read_file_as_str('TOKEN')
print (TOKEN)
updater = Updater(token=TOKEN, use_context=True)
dispatcher = updater.dispatcher

start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

echo_handler = MessageHandler(Filters.text & (~Filters.command),echo)

dispatcher.add_handler(echo_handler)

updater.start_polling()
