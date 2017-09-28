import telepot, time, extraFunctions
import praw
from random import randint, choice
redditBot = telepot.Bot('311373108:AAGjGzz5iuaU4fztrgga6o9o7EvjHEVjBEQ')
Subreddit = ''
urlSearch = ['.jpg', '.gif', 'youtu.be']
r = praw.Reddit\
        (
            client_id='UgNTA08lWUu5MA',
            client_secret="57bVffIOhVD_MvaIeBeu_gvIVzQ",
            password="Password1",
            user_agent='jkfl;',
            username="stplusearthpornbot"
        )
def handleSubreddit(Subreddit, chat_id, random) :
    y=0
    if random == 1 :
        randPost = []
        randLink = []
        rand = 0
        sub = r.subreddit(Subreddit)
        for submission in sub.hot(limit=100):
            if str(submission.url) in urlSearch :
                randPost.append(submission.title)
                randLink.append(submission.url)
                y += 1
        x = randint(1 , y-1)
        y=0
        redditBot.sendMessage(chat_id, randPost[x])
        redditBot.sendMessage(chat_id, randLink[x])
        randPost = []
        randLink = []
    if random == 0 :
        if Subreddit == '' :
            sub = r.random_subreddit(nsfw=False)
            redditBot.sendMessage(chat_id, sub.display_name)
            print(sub.display_name)
        elif Subreddit == '/fetchtop' :
            sub = r.random_subreddit(nsfw=False)
            redditBot.sendMessage(chat_id, sub.display_name)
            print(sub.display_name)
        else :
            sub = r.subreddit(Subreddit)
        for submission in sub.hot(limit=20) :
            if '.jpg' in str(submission.url) :
                redditBot.sendMessage(chat_id, submission.title)
                redditBot.sendMessage(chat_id, submission.url)
                break
            elif '.gif' in str(submission.url) :
                redditBot.sendMessage(chat_id, submission.title)
                redditBot.sendMessage(chat_id, submission.url)
                break
            elif 'youtu.be' in str(submission.url) :
                redditBot.sendMessage(chat_id, submission.title)
                redditBot.sendMessage(chat_id, submission.url)
                break

def handle(msg) :
    #Checking response types
    content_type, chat_type, chat_id = telepot.glance(msg)
    print(chat_id)
    #Prints a few things
    print(content_type, chat_type, chat_id)

    if content_type == 'text':
        if '/fahrenheit' in str(msg).lower() :
            msg = msg['text']
            while ' ' in msg:
                msg = msg[1:]
            msg = int(msg)
            celsius = int(msg * 9/5 + 32)
            msg = str(celsius) + ' °F'
            redditBot.sendMessage(chat_id, msg)
        if '/celsius' in str(msg).lower() :
            msg = msg['text']
            while ' ' in msg:
                msg = msg[1:]
            msg = int(msg)
            fahrenheit = int((msg-32)*5/9)
            msg = str(fahrenheit) + ' °C'
            redditBot.sendMessage(chat_id, msg)
        if '/start' in str(msg).lower() :
            redditBot.sendMessage(chat_id, 'Welcome! To search for a subreddit, type /FetchTop and type your subreddit in! (ex. /r/ShowerThoughts).'
                                           ' Posts that only have selftext do not work yet.\nTo get a random subreddit, type /FetchTop with nothing'
                                           ' afterwards. For more commands, type /help.')

        if 'do you work for the government' in str(msg).lower() :
            redditBot.sendMessage(chat_idr, "Access Denied.")
        if '/help' in str(msg).lower() :
            redditBot.sendMessage(chat_id, '/help - Opens this text \n'
                                           '/fetchtop (Subreddit) - Fetches the top post of a given subreddit, if a random sub is wanted, leave (subreddit) blank. \n'
                                           '/fetchrandom (subreddit) - Gives a random post from a given subreddit.\n'
                                           '/Quote - Gives a random /r/showerthoughts\n'
                                           'These are all case insensitive!')

        if '/quote' in str(msg).lower() :
            Quotes = 'Showerthoughts'
            sub = r.subreddit(Quotes)
            randQuote = []
            for submission in sub.hot(limit = 20) :
                randQuote.append(submission.title)
            redditBot.sendMessage(chat_id, choice(randQuote))
            randQuote = []
        if '/fetchrandom' in str(msg).lower() :
            msg = extraFunctions.extractMessage(msg['text'])
            print(msg)
            try :
                handleSubreddit(msg, chat_id, 1)
            except :
                redditBot.sendMessage(chat_id, 'Subreddit not found or has no posts. Did you misspell the subreddit? If not, Omegaxys screwed up, blame him.')
        if '/fetchtop' in str(msg).lower() :
            msg = extraFunctions.extractMessage(msg['text'])
            print(msg)
            try :
                handleSubreddit(msg, chat_id, 0)
            except :
                redditBot.sendMessage(chat_id, 'Subreddit not found or has no posts. Did you misspell the subreddit? If not, Omegaxys screwed up, blame him.')

redditBot.message_loop(handle)
while True:
    time.sleep(10)