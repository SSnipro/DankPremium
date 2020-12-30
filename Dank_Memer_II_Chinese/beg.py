import random
from telegram.ext import Dispatcher,CommandHandler
def begging(update, context):
    Names = ["一个傻子", "傻丽", "唐老鸭", "你妈", "Dank Memer II", "鲍勃", "萨莉", "黄老师", "像蒋思成的人", "空气"]
    Money = random.randint(0,200)
    msg6 = ("%s 给你捐赠了 %s XP!\n\nAuthorised By Noah <3\n作者：Noah"%(random.choice(Names),Money))
    update.message.reply_text(msg6)
 

def add_handler(dp:Dispatcher):
    beg_handler = CommandHandler('DCBeg',begging)
    dp.add_handler(beg_handler)





