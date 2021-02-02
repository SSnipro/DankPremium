from telegram.ext import Dispatcher,CommandHandler,CallbackQueryHandler
from telegram import BotCommand,InlineKeyboardMarkup,InlineKeyboardButton
from Utilities import util
import random

fkb = [{
    '➡️':'f:forward'},{
    '🔀':'f:skip',
    '🎵':'f:audio'
}]

kb = util.getkb(fkb)

disc = {
    's1': {
        'q1':[
            "Question: Y a-t-il un ou une humoriste que tu aimes particulièrement?",
            "Mon humoriste préféré c’est Mark Twain.  Je pense qu'il est très drôle. J'aime particulièrement le livre qu'il a écrit intitulé « Les aventures de Tom Sawyer».  J'ai aussi entendu des histoires à son sujet qui sont vraiment drôles. Et toi Emily? ",
            "Emily talks",
            "Simon talks", 
            "Ah oui j’aime bien « Mr Bean » aussi.", 
            "Michael talks"],
        'q2':[
            "Question Simon: Est-ce que la bonne humeur c’est une grosse partie de ta vie?",
            "Oui. Je pense que l’humour est de bonne humeur. Et l'humour est une partie très importante de ma vie.  Sans humour, la vie serait ennuyeuse. Quand nos amis sont malheureux, nous inventons une blague et sortons simplement de l'humeur malheureuse. Mes amis et moi faisions des blagues humoristiques et rions ensemble.  C'est un moment vraiment amusant.",
            "Emily talks",
            "Simon talks",
            "Michael talks"
        ],
        'q3':[
            "Question Emily: Quels genres d’humour préfères-tu?",
            "Je n'ai pas vraiment de genre d'humour préféré parce que je ne regarde pas vraiment les émissions d'humour, mais je pense que si j'avais un genre d'humour préféré, ce serait la comédie physique. Je pense que la comédie physique sera mon type d'humour préféré car j'aime les clowns.  Ils sont drôles.",
            "Emily talks",
            "Simon talks",
            "Michael talks"
        ],
        'q4':[
            "Question Michael: Est-ce que tu détestes l'humeur, où est ce que tu l’aime?",
            "Noah: Il y a beaucoup de bonnes choses dans l'humour.  Cela pourrait vous donner une humeur positive au lieu d'être d'humeur négative comme Mr Bean, quand j’ai un mauvais sentiment, je vais le regarder. Cependant, certains types d'humour sont violents et inappropriés.",
            "Emily talks",
            "Simon talks",
            "Michael talks"
        ]
    },
    's2': {
        'q1':[],
        'q2':[],
        'q3':[],
        'q4':[]
    }
}
msg = []
def fr(update,context):
    f = ""
    chatid = update.effective_chat.id
    uid = str(update.effective_user.id)
    ss = ['s1','s2']
    s = random.choice(ss)
    if uid == "1360440667":
        for i in list(disc[s]):
            for j in list(disc[s][i]):
                msg.append(f"-{j}")
        update.message.reply_text(msg[0],reply_markup=kb)
    else: 
        update.message.reply_text("Your not Noah!")

def buttonCallback(update, context):
    query = update.callback_query 
    chatid = update.effective_chat.id
    user = update.effective_user
    if not str(user.id) == '1360440667':
        update.message.reply_text("Your not Noah!")
        return
    if query.data == 'f:audio':
        query.answer("Audio not ready yet!")
    elif query.data == 'f:forward':
        msg.pop(0)
        for k in msg:
            query.edit_message_text(k,reply_markup=kb)
            break
    elif query.data == 'f:skip':
        pass

def add_handler(dp:Dispatcher):
    dp.add_handler(CommandHandler('frenchdisscusion', fr))
    dp.add_handler(CallbackQueryHandler(buttonCallback,pattern="^f:[A-Za-z0-9_]*"))