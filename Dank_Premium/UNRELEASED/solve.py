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
      msg9 += "Did you write all your answers for your english homework in your math homework?"
  elif d == mm:
      msg9 += "%s * %s = %s"%(a, c, float(a*c))
      msg9 += "\nYou got %s XP for doing your math homework. \n\nAuthorised By Noah <3\n作者：Noah"%(random.randint(50,100))
  elif d == aa:
      msg9 += "%s + %s = %s"%(a, c, float(a+c))
      msg9 += "\nYou got %s XP for doing your math homework. \n\nAuthorised By Noah <3\n作者：Noah"%(random.randint(50,100))
  elif d == ss:
      msg9 += "%s - %s = %s"%(a, c, float(a-c))
      msg9 += "\nYou got %s XP for doing your math homework. \n\nAuthorised By Noah <3\n作者：Noah"%(random.randint(50,100))
  elif c != 0 and d == dd:
      msg9 += "%s / %s = %s"%(a, c, float(a/c))
      msg9 += "\nYou got %s XP for doing your math homework. \n\nAuthorised By Noah <3\n作者：Noah"%(random.randint(50,100))
  elif c == 0:
      msg9 += "WHAT DO YOU THINK YOUR DOING DIVIDING BY ZERO? YOU FAILED YOUR MATH TEST AND LOST 200 XP"
  update.message.reply_text(msg9)

def add_handler(dp:Dispatcher):
    solve_handler = CommandHandler('DSolve',solving)
    dp.add_handler(solve_handler)
