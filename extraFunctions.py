import telepot
redditBot = telepot.Bot('311373108:AAGjGzz5iuaU4fztrgga6o9o7EvjHEVjBEQ')


def extractMessage(msg) :
    if '/' in msg[1:]:
        while '/' in str(msg).lower():
            msg = msg[1:]
    else:
        while ' ' in msg:
            msg = msg[1:]
    return msg

def messageSend(title, url, id) :
    redditBot.sendMessage(id, title)
    redditBot.sendMessage(id, url)