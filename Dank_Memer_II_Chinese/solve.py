import random
from telegram.ext import Dispatcher,CommandHandler, ConversationHandler

def solving(update, context):
  msg9 = ""
  mm = str("*")
  aa = str("+")
  ss = str("-")
  dd = str("/")
  b = update.message.text
  a = float(b.split()[1])
  c = float(b.split()[3])
  d = str(b.split()[2])
  if d != mm and d != aa and d != ss and d != dd:
      msg9 += "难道你把英语作业的答案都写到数学作业上面了吗？！"
  elif d == mm:
      msg9 += "%s * %s = %s"%(a, c, float(a*c))
      msg9 += "\n你做完了你的数学作业，被奖励了 %s XP。 \n\nAuthorised By Noah <3\n作者：Noah"%(random.randint(50,100))
  elif d == aa:
      msg9 += "%s + %s = %s"%(a, c, float(a+c))
      msg9 += "\n你做完了你的数学作业，被奖励了 %s XP。 \n\nAuthorised By Noah <3\n作者：Noah"%(random.randint(50,100))
  elif d == ss:
      msg9 += "%s - %s = %s"%(a, c, float(a-c))
      msg9 += "\n你做完了你的数学作业，被奖励了 %s XP。 \n\nAuthorised By Noah <3\n作者：Noah"%(random.randint(50,100))
  elif c != 0 and d == dd:
      msg9 += "%s / %s = %s"%(a, c, float(a/c))
      msg9 += "\n你做完了你的数学作业，被奖励了 %s XP。 \n\nAuthorised By Noah <3\n作者：Noah"%(random.randint(50,100))
  elif c == 0:
      msg9 += "你想什么呢？？？？？除零？？？？你数学考试没及格"
  update.message.reply_text(msg9)

def add_handler(dp:Dispatcher):
    solve_handler = CommandHandler('DSolve',solving)
    dp.add_handler(solve_handler)
