import sys
import time
import random
import datetime
import telepot
import requests

def handle(msg):
    chat_id = msg['chat']['id']
    command = msg['text']

    print 'Got command: %s' % command

    if command == '/roll':
        bot.sendMessage(1061745573, random.randint(1,6))
    elif command == '/time':
        bot.sendMessage(1061745573, str(datetime.datetime.now()))
    


bot = telepot.Bot('998729622:AAEXjepiJd-aTL5bO6wqHKBc3EciDTyniJ0')
bot.message_loop(handle)
print 'I am listening ...'

while 1:
    time.sleep(10)