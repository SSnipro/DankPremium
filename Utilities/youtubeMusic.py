from telegram.ext import Dispatcher,CommandHandler,CallbackQueryHandler
from telegram import BotCommand
import pafy,os


def youtubemusic(update,context):
    if len(context.args) == 1:
        url = context.args[0]
        video = pafy.new(url)
        update.message.reply_text(str(video) )
    else:
        update.message.reply_text("Put a link! for example: /pd_yt_music@dankpbot https://www.youtube.com/watch?v=BezpUnoZObw")

def musicOnly(update,context):
    if len(context.args) == 1:
        # url = str(context.args[0])
        # video = pafy.new(url)
        # v = str(video).split('\n')
        # title = v[0]
        # author = v[1]
        # print(v)
        # for n in video.streams:
        #     print(f'LOL ITS THIS -> \n{n}\n\n')
        # audiostreams = video.audiostreams
        # for a in audiostreams:
        #     print(a.bitrate, a.extension, a.get_filesize())
        # update.message.reply_text
        if 'www.youtube.com' in url:
            video = pafy.new(url)
            print (video.length)
            if video.length <= 6000:
                bestaudio = video.getbestaudio(preftype="m4a")
                audiofile = f'/tmp/{bestaudio.title}.{bestaudio.extension}'
                bestaudio.download(audiofile)
                update.message.reply_audio(open(audiofile, 'rb'),caption=f'{title}\n{author}\n\n')
                os.remove(audiofile)
    
    else:
        update.message.reply_text("Put a link! for example: /pdgetmusic@dankpbot https://www.youtube.com/watch?v=BezpUnoZObw")

def add_handler(dp:Dispatcher):
    dp.add_handler(CommandHandler('pd_yt_music', youtubemusic))
    dp.add_handler(CommandHandler('pdgetMusic', musicOnly))

if __name__ == "__main__":  
    url = "https://www.youtube.com/watch?v=BezpUnoZObw"
    # url = str(context.args[0])
    video = pafy.new(url)
    v = str(video).split('\n')
    title = v[0]
    author = v[1]
    print(v)
    p = video.m4astreams
    for n in video.streams:
        print(n)
    bestaudio = video.getbestaudio(preftype="m4a")
    print(bestaudio)
    file_path = f"/images/{bestaudio.title}.{bestaudio.extension}"
    bestaudio.download(filepath=file_path)
            