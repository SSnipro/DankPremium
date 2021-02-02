import random
from telegram.ext import Dispatcher,CommandHandler
from telegram.ext import Updater
from telegram.ext import MessageHandler, Filters, Updater
from telegram import BotCommand
from Currency import bal,work,shop
from Currency.UNRELEASED import twentyFour,leaderboards,search
from Currency.LIST import lst
from Currency.LIST.Adventure import adventure
from Currency.LIST.Adventure.Arctic import arctic
from Currency.LIST.Adventure.Arctic.Stores import Cheap,Better
from Currency.LIST.Adventure.Wilderness import hunt, cliff, wild
from Currency.LIST.Adventure.Wilderness.followPath import followPath, fish 
from Currency.LIST.Adventure.Space import space, decline
from Currency.LIST.Adventure.Space.Yes import accept, fly
from Currency.Games import bj
# from Fun import punish,gif
from Fun.UNRELEASED import french
from Utilities import mysystemd, youtubeMusic
from Utilities.Apple_Calendar import DankCalendar, setCalendar, helpCalendar
from Utilities.get_file_info import animationInfo, fileInfo
from Utilities.UNRELEASED import team
import os


def start(update, context):
    update.message.reply_text("""

Sup! My name is Dank Premium. Authorized by Telegram User SSnipro (Just call him Noah it's fine).
Dank Premium provides lots of amazing features. You can do many things to try  to get much $ as you want!
    
Also, Noah will try to add some new features really soon!
    
Enjoy!
    
--------------------
Commands:

    Currency:

        💼 /PDWork - Submit your work to your boss. Depending on your work quality, you will either receive an reward or punishment.
        🏦 /PDBal - Check your current balence!
        🛒 /PDShop - Buy equipment
        👜 /PDInv - Check your inventory!
        🎁 /PDDaily - Collect your daily coins!

        Games:
            🃏 /PDBJ - Play a Blackjack game against 🤖 DMII and your friends!

        List:
            /PDList
            🔫 /PDHunt - Hunt em down!!!!!!
            🎣 /PDFish - Try your luck by fishing!
        
    Fun:

        🤡 /PDGif - Funny gifs! (💎 ~🚧 Function under construction 🚧~ 💎 Sorry! ~)
        👹 /PDPunish - get rekt in Classcraft you fool (💎 ~🚧 Function under construction 🚧~ 💎 Sorry! ~)

    Utils: 

        🌠 /PDAInfo - Information about an image / animation sent in telegram!
        🎆 /PDFInfo - Information about any file! Reply to do so!

        
    UNRELEASED:

        🎯 /PDLeaderboards - Richest people on the server! (💎 ~🚧 Function under construction 🚧~ 💎 Sorry! ~)
        ✅ /PDList - Look at a list of things you can do!
        ♦️ /PDGuess - Play a game of guess (version.1.0)
        ♠️ /PDGuessB - Play a game of guess (version.2.0)
        ♥️ /PDGuessB2 - Play a game of guess (version.2.1)
        ♣️ /PDGuessBwHD - Play a game of guess (version.HD)
        🥺 /PDBeg - beg loser
        🎰 /PD24 - Play a game of 24! (Adding rules later)

        🕵🏻‍♂️ /PDSearch - Search the area with your team! Be prepared to fight stuff...
        🧮 /PDSolve - Just a normie calculator no big deal
        👔 /PDUseCodes - gifted codes!

--------------------
    """)

def read_file_as_str(file_path): 
    if not os.path.isfile(file_path):
        raise TypeError(file_path + " does not exist")
    all_the_text = open(file_path).read()
    return all_the_text

def get_command():
    return [BotCommand('pdinfo','Information')]

TOKEN = read_file_as_str('TOKEN')
updater = Updater(token=TOKEN, use_context=True)
dispatcher = updater.dispatcher

start_handler = CommandHandler('start', start)
info_handler = CommandHandler('PDInfo', start)

dispatcher.add_handler(start_handler)
dispatcher.add_handler(info_handler)

# Currency

bal.add_handler(dispatcher)
work.add_handler(dispatcher)
bj.add_handler(dispatcher)
hunt.add_handler(dispatcher)
fish.add_handler(dispatcher)
leaderboards.add_handler(dispatcher)
adventure.add_handler(dispatcher)
lst.add_handler(dispatcher)
cliff.add_handler(dispatcher)
followPath.add_handler(dispatcher)
wild.add_handler(dispatcher)
arctic.add_handler(dispatcher)
Better.add_handler(dispatcher)
Cheap.add_handler(dispatcher)
space.add_handler(dispatcher)
decline.add_handler(dispatcher)
accept.add_handler(dispatcher)
fly.add_handler(dispatcher)
shop.add_handler(dispatcher)
french.add_handler(dispatcher)

# punish.add_handler(dispatcher)
# gif.add_handler(dispatcher)
# twentyFour.add_handler(dispatcher)
# search.add_handler(dispatcher)

# Utils

animationInfo.add_handler(dispatcher)
fileInfo.add_handler(dispatcher)

youtubeMusic.add_handler(dispatcher)
team.add_handler(dispatcher)

DankCalendar.add_handler(dispatcher)
setCalendar.add_handler(dispatcher)
helpCalendar.add_handler(dispatcher)

commands = work.get_command() + bal.get_command() + bj.get_command() + get_command() + hunt.get_command() + fish.get_command() + lst.get_command() + shop.get_command()
bot = updater.bot
bot.set_my_commands(commands)

updater.start_polling()
print('Started')
mysystemd.ready()

DankCalendar.run_repeating(updater.job_queue)

updater.idle()
print('Stopping...')
print('Stopped.')