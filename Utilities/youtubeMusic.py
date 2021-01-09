import random
from telegram.ext import Dispatcher,CommandHandler
from telegram import BotCommand
from Currency import bal

def ym(update,context):
    pass

def add_handler(dp:Dispatcher):
    reward_handler = CommandHandler('pdytmusic', ym)
    dp.add_handler(reward_handler)

if __name__ == "__main__":
    pass
