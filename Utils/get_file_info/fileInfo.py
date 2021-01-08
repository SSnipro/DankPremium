from telegram import Update, Animation, PhotoSize, Voice, Audio, Document, Video, Sticker, Game, VideoNote
from telegram.ext import Dispatcher,CommandHandler,CallbackContext
from json import dumps,loads

def read_file(update, context):
    if update.message.reply_to_message:
        if update.message.reply_to_message.animation:
            file_id = str(update.message.reply_to_message.animation.file_id)
            unique_id = str(update.message.reply_to_message.animation.file_unique_id)
            width = str(update.message.reply_to_message.animation.width)
            height = str(update.message.reply_to_message.animation.height)
            duration = str(update.message.reply_to_message.animation.duration) 
            # context.bot.send_message(update.effective_user.id,text=f"file_id = '{file_id}', \nfile_unique_id = '{unique_id}', \nwidth = {width}, \nheight = {height}, \nduration = {duration}")
            animation = Animation(file_id,unique_id,width,height,duration)
            update.message.reply_animation( animation , caption=f"This is an animation. \n\n\nfile_id = '{file_id}', \n\nfile_unique_id = '{unique_id}', \n\nwidth = {width}, \n\nheight = {height}, \n\nduration = {duration}")
        if update.message.reply_to_message.photo:
            file_id = str(update.message.reply_to_message.photo[2]['file_id'])
            unique_id = str(update.message.reply_to_message.photo[2]['file_unique_id'])
            width = str(update.message.reply_to_message.photo[2]['width'])
            height = str(update.message.reply_to_message.photo[2]['height'])
            file_size = str(update.message.reply_to_message.photo[2]['file_size'])
            photo = PhotoSize(file_id,unique_id,width,height,file_size)
            update.message.reply_photo( photo , caption=f"This is a photo. \n\n\nfile_id = '{file_id}', \n\nfile_unique_id = '{unique_id}', \n\nwidth = {width},\n\nheight = {height},\n\nfile_size = {file_size}\n\n")
        if update.message.reply_to_message.voice:
            file_id = str(update.message.reply_to_message.voice.file_id)
            unique_id = str(update.message.reply_to_message.voice.file_unique_id)
            duration = str(update.message.reply_to_message.voice.duration)
            mime_type = str(update.message.reply_to_message.voice.mime_type)
            file_size = str(update.message.reply_to_message.voice.file_size)
            voice = Voice(file_id,unique_id,duration,mime_type,file_size)
            update.message.reply_voice( voice, caption=f"This is a voice message. \n\n\nfile_id = '{file_id}', \n\nfile_unique_id = '{unique_id}', \n\nduration = {duration},\n\nmime_type = {mime_type},\n\nfile_size = {file_size}\n\n")
        if update.message.reply_to_message.audio:
            file_id = str(update.message.reply_to_message.audio.file_id)
            unique_id = str(update.message.reply_to_message.audio.file_unique_id)
            duration = str(update.message.reply_to_message.audio.duration)
            performer = str(update.message.reply_to_message.audio.performer)
            title = str(update.message.reply_to_message.audio.title)
            mime_type = str(update.message.reply_to_message.audio.mime_type)
            file_size = str(update.message.reply_to_message.audio.file_size)
            audio = Audio(file_id,unique_id,duration,performer,title,mime_type,file_size)
            update.message.reply_audio( audio, caption=f"This is an audio. \n\n\nfile_id = '{file_id}', \n\nfile_unique_id = '{unique_id}', \n\nduration = {duration},\n\nperformer = {performer} \n\ntitle = {title}, \n\nmime_type = {mime_type},\n\nfile_size = {file_size}")
        if update.message.reply_to_message.document:
            file_id = str(update.message.reply_to_message.document.file_id)
            unique_id = str(update.message.reply_to_message.document.file_unique_id)
            document = Document(file_id,unique_id)
            update.message.reply_document( document, caption=f"This is a document. \n\n\nfile_id = '{file_id}',\n\nfile_unique_id = '{unique_id}'")
        if update.message.reply_to_message.video:
            file_id = str(update.message.reply_to_message.video.file_id)
            unique_id = str(update.message.reply_to_message.video.file_unique_id)
            width = str(update.message.reply_to_message.video.width)
            height = str(update.message.reply_to_message.video.height)
            duration = str(update.message.reply_to_message.video.duration)
            video = Video(file_id,unique_id,width,height,duration)
            update.message.reply_video( video, caption=f"This is a video. \n\n\nfile_id = '{file_id}',\n\nfile_unique_id = '{unique_id}', \n\nwidth = {width}, \n\nheight = {height},\n\nduration = {duration}")
        if update.message.reply_to_message.sticker:
            file_id = str(update.message.reply_to_message.sticker.file_id)
            unique_id = str(update.message.reply_to_message.sticker.file_unique_id)
            width = str(update.message.reply_to_message.sticker.width)
            height = str(update.message.reply_to_message.sticker.height)
            is_animated = str(update.message.reply_to_message.sticker.is_animated)
            sticker = Sticker(file_id,unique_id,width,height,is_animated)
            update.message.reply_sticker( sticker, caption='')
            context.bot.send_message(update.effective_chat.id, text=f"This is a sticker. \n\n\nfile_id = '{file_id}',\n\nfile_unique_id = '{unique_id}', \n\nwidth = {width}, \n\nheight = {height},\n\nis_animated = {is_animated}")
        if update.message.reply_to_message.game:
            title = str(update.message.reply_to_message.game.title)
            description = str(update.message.reply_to_message.game.description)
            photo = str(update.message.reply_to_message.game.photo)
            text = str(update.message.reply_to_message.game.text)
            text_entities = str(update.message.reply_to_message.game.text_entities)
            animation = str(update.message.reply_to_message.game.animation)
            game = Game(title,description,photo,text,text_entities,animation)
            update.message.reply_game( game ,caption=f'This is a game.\n\n\ntitle = {title}, \n\ndescription = {description}, \n\nphoto = {photo}, \n\ntext = {text}, \n\ntext_entities = {text_entities}, \n\nanimation = {animation}')
        if update.message.reply_to_message.video_note:
            file_id = str(update.message.reply_to_message.video_note.file_id)
            unique_id = str(update.message.reply_to_message.video_note.file_unique_id)
            length = str(update.message.reply_to_message.video_note.length)
            duration = str(update.message.reply_to_message.video_note.duration)
            videoNote = VideoNote(file_id,unique_id,length,duration)
            update.message.reply_video_note( videoNote, caption='')
            context.bot.send_message(update.effective_chat.id, text=f"This is a video message.\n\n\nfile_id = '{file_id}',\n\nfile_unique_id = '{unique_id}',\n\nlength = {length}, \n\nduration = {duration}")
        if update.message.reply_to_message.text:
            ttext = str(update.message.reply_to_message.text)
            update.message.reply_text(f'{ttext}\n\nThis is a text.')
    else: 
        u = str(update)
        u = dumps(eval(u),indent=2)
        update.message.reply_text(u)
       
   
def add_handler(dp:Dispatcher):
    dp.add_handler(CommandHandler('pdfinfo', read_file))


