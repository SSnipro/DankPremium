from telegram import Update,Animation, PhotoSize
from telegram.ext import Dispatcher,CommandHandler,CallbackContext
from json import dumps,loads

msg_type = {
    "video":["file_id","file_unique_id","width","height","duration"],
    "photo":["file_id","file_unique_id","width","height","file_size"],
    "audio":["file_id","file_unique_id","width","height","file_size"],
    "animation":["file_id","file_unique_id","width","height","duration"],
    "sticker":["file_id","file_unique_id","width","height","is_animated"],
    "videomsg":["file_id","file_unique_id","length","duration"],
    "voicemsg":["file_id","file_unique_id","duration","mime_type","file_size"]
}

def listtojson(objs):
    r = ""
    count = 0
    for obj in objs:
        count += 1
        r += f"\n第{count}个"
        r += tojson(obj)
    return r

def tojson(obj):
    return dumps(eval(str(obj)),indent=2)

def getobjinfo (msgtype,msgobj):
    rmsg = ""
    for i in msg_type[msgtype]:
        rmsg += str(f'{i} = {msgobj.__dict__[i]},\n\n')
    return rmsg

def info(update:Update,context: CallbackContext):
    if update.effective_message.reply_to_message:
        msg = update.effective_message.reply_to_message
        msg_attr = {}
        rmsg = ""
        if msg.audio:
            audio = update.message.reply_to_message.audio
            rmsg = getobjinfo('audio',audio)
        if msg.animation:
            animation = update.message.reply_to_message.animation
            rmsg = getobjinfo('animation',animation)
            update.message.reply_animation(animation,caption=rmsg)
        # if msg.photo:
        #     msg_attr["Photo"] = listtojson(msg.photo)
        # if msg.video:
        #     msg_attr["Video"] = tojson(msg.video)
        # if len(msg_attr)==0:
        # #     msg_attr["不知道是什么东东"] = tojson(msg)
        # r = ""
        # for a in msg_attr:
        #     r = f"类型：{a}\n{msg_attr[a]}\n"
        # update.message.reply_text(text=r)
    else:
        update.message.reply_text(text=tojson(update.effective_message))

def hdinfo(update:Update,context: CallbackContext):
    update.message.reply_text(text=tojson(update.effective_message))

def add_dispatcher(dp: Dispatcher):
    dp.add_handler(CommandHandler(["info"], info))
    dp.add_handler(CommandHandler(["hdinfo"], hdinfo))