from telegram.ext import Dispatcher,CommandHandler,CallbackQueryHandler
from telegram import BotCommand
import pafy

def youtubemusic(update,context):
    if len(context.args) == 1:
        url = context.args[0]
        video = pafy.new(url)
        update.message.reply_text(str(video) )
    else:
        update.message.reply_text("help!")

def add_handler(dp:Dispatcher):
    dp.add_handler(CommandHandler('pdytmusic', youtubemusic))

if __name__ == "__main__":
    url = "https://www.youtube.com/watch?v=iqL1BLzn3qc"