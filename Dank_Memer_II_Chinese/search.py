import random
from telegram.ext import Dispatcher,CommandHandler
import bal

def searching(update, context):
    Search = ["你在空气里找到了一些新元素。你得到了 300 XP。", "你抢劫了银行并得到了 120 XP。快跑!!!!!", "你尝试去抢劫银行却被警察击中。下次练完躲避球再来吧。", "你在路上讨钱。你忘了他们不再给讨钱的人 XP 了么？", "你搜索了学校但被误以为一个拐卖小孩的骗子。你入狱了。", "你搜索了医院，但被流感传染。你挂了。", "你搜索了医院并找到了一名医生的包。你获得了 20 XP。", "你在阁楼找到了 40 XP。在这里待了多久了？", "你搜索了鬼屋并找到了一个金库。你打开了它并找到了 1000 XP！幸好里面没有鬼。", "你搜索了一棵树并找到了一批宝藏。你得到了 270 XP。 酷！", "你搜索了 L - 公园，最终收获了 9 XP。", "你尝试去搜索鬼屋。 你被 幽灵 给击败了。"]
    msg4 = random.choice(Search)
    if msg4 == Search[0]:
        bal.bal += 300
    elif msg4 == Search[1]:
        bal.bal += 120
    elif msg4 == Search[6]:
        bal.bal += 20
    elif msg4 == Search[7]:
        bal.bal += 40
    elif msg4 == Search[8]:
        bal.bal += 1000
    elif msg4 == Search[9]:
        bal.bal += 270
    elif msg4 == Search[10]:
        bal.bal += 9
    msg4 += "\n\nAuthorised By Noah <3\n作者：Noah"
    update.message.reply_text(msg4)

def add_handler(dp:Dispatcher):
    search_handler = CommandHandler('DCSearch', searching)
    dp.add_handler(search_handler)



