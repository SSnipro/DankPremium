from telegram import Update, Animation, PhotoSize
from telegram.ext import Dispatcher,CommandHandler,CallbackContext
from json import dumps,loads

def read_animation(update, context):
    if update.message.reply_to_message:
        if update.message.reply_to_message.animation:
            file_id = str(update.message.reply_to_message.animation.file_id)
            unique_id = str(update.message.reply_to_message.animation.file_unique_id)
            width = str(update.message.reply_to_message.animation.width)
            height = str(update.message.reply_to_message.animation.height)
            duration = str(update.message.reply_to_message.animation.duration) 
            # context.bot.send_message(update.effective_user.id,text=f"file_id = '{file_id}', \nfile_unique_id = '{unique_id}', \nwidth = {width}, \nheight = {height}, \nduration = {duration}")
            animation = Animation(file_id,unique_id,width,height,duration)
            update.message.reply_animation( animation , caption=f"file_id = '{file_id}', \n\nfile_unique_id = '{unique_id}', \n\nwidth = {width}, \n\nheight = {height}, \n\nduration = {duration}")
        else:
            update.message.reply_text('Incorrect format! Try /pdpinfo@dankpbot if it was an image!')
    else:
        update.message.reply_text('Incorrect format!')

def read_pic(update,context):
    if update.message.reply_to_message:
        if update.message.reply_to_message.photo:
            file_id = str(update.message.reply_to_message.photo[0]['file_id'])
            unique_id = str(update.message.reply_to_message.photo[0]['file_unique_id'])
            width = str(update.message.reply_to_message.photo[0]['width'])
            height = str(update.message.reply_to_message.photo[0]['height'])
            file_size = str(update.message.reply_to_message.photo[0]['file_size'])
            photo = PhotoSize(file_id,unique_id,width,height,file_size)
            update.message.reply_photo( photo , caption=f"file_id = '{file_id}', \n\nfile_unique_id = '{unique_id}', \n\nwidth = {width},\n\nheight = {height},\n\nfile_size = {file_size}\n\n")
        else:
            update.message.reply_text('Incorrect format! Try /pdainfo@dankpbot if it was an animation!')
    else:
        update.message.reply_text('Incorrect format!')


def add_handler(dp:Dispatcher):
    dp.add_handler(CommandHandler('pdainfo', read_animation))
    dp.add_handler(CommandHandler('pdpinfo', read_pic))


