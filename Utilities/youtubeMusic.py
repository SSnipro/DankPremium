from telegram.ext import Dispatcher,CommandHandler,CallbackQueryHandler
from telegram import BotCommand, InputMediaAudio
import pafy
import os
import re

def youtubemusic(update,context):
    if len(context.args) == 1:
        url = context.args[0]
        video = pafy.new(url)
        update.message.reply_text(str(video) )
    else:
        update.message.reply_text("Put a link! for example: /pd_yt_music@dankpbot https://www.youtube.com/watch?v=r_a4Zg3PyA0")

def validateTitle(title):
    rstr = r"[\/\\\:\*\?\"\<\>\|]"  # '/ \ : * ? " < > |'
    new_title = re.sub(rstr, "", title)  # 替换为下划线
    return new_title

def musicOnly(update,context):
    if len(context.args) == 1:
        url = str(context.args[0])
        if 'youtube.com' in url or 'youtu.be' in url:
            chatid = update.effective_chat.id
            video = pafy.new(url)
            v = str(video).split('\n')
            title = v[0].split(':')[1]
            author = v[1].split(':')[1]
            bestaudio = video.getbestaudio(preftype="m4a")
            music_size = bestaudio.get_filesize()
            audio = f'{bestaudio.title}'
            audiofile = f'/tmp/{validateTitle(audio)}.{bestaudio.extension}'
            if music_size < 1000*1000*10:
                img = "https://i.pcmag.com/imagery/articles/04oP7J3OIykTchX4vhU57vn-28..1569485834.jpg"
                bestaudio.download(audiofile)
                msg = update.message.reply_photo(img,f"downloading... Your audio's size is {music_size/100}KB\n\n🎵 Music: {title} by 🎶 {author}")
                msg.edit_media(InputMediaAudio(open(audiofile,'rb')))
                msg == context.bot.send_message(chatid,f"{str(video)}")
                os.remove(audiofile)
            else: 
                update.message.reply_text("Sorry this file is too big")
        else:
            update.message.reply_text("Youtube Video Link Please!")
    else:
        update.message.reply_text("Put a link! for example: /pdgetmusic@dankpbot https://www.youtube.com/watch?v=r_a4Zg3PyA0")

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
            