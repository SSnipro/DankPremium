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
    dp.add_handler(CommandHandler('pd_yt_music', youtubemusic))

if __name__ == "__main__":
    url = "https://www.youtube.com/watch?v=BezpUnoZObw"
    video = pafy.new(url)
    for n in video.streams:
        print(n)
    bestaudio = video.getbestaudio(preftype="m4a")
    print(bestaudio)
    file_path = f"/tmp/{bestaudio.title}.{bestaudio.extension}"
    # bestaudio.download(filepath=file_path)