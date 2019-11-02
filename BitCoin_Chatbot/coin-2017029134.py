import requests
import datetime
import ast
import json
import csv
import telepot
import time
from apscheduler.schedulers.background import BlockingScheduler

#function that Get the price from url.
def price(symbol, comparison_symbols=[''], exchange=''):
    url = 'https://min-api.cryptocompare.com/data/price?fsym={}&tsyms={}'\
        .format(symbol.upper(), ','.join(comparison_symbols).upper())
    if exchange:
        url += '&e={}'.format(exchange)
    page = requests.get(url)
    data = page.json()
    return data

# function that write the price in csv file and execute the Sent_to_bot() function.
def write_price():
    now = datetime.datetime.now()
    nowDatetime = now.strftime('%Y-%m-%d %H:%M:%S')

    price1 = ast.literal_eval(json.dumps(price('BTC', ['USD'], exchange='Bitfinex')))['USD']
    price2 = ast.literal_eval(json.dumps(price('BTC', ['KRW'], exchange='Bithumb')))['KRW']

    # send the price2 value and send to bot
    Send_to_bot(price2)

    with open('BitCoin.csv', 'a') as csvfile:
        fieldnames = ['Date', 'Bitfinex-USD', 'Bithum-KRW']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerow({'Date': nowDatetime, 'Bitfinex-USD': price1, 'Bithum-KRW': price2})

# global variable PRE_price is previous price to calculate UP.
PRE_price = 0
# function to send the price and UP
def Send_to_bot(price2):
    global PRE_price
    bot = telepot.Bot('***********************************')

    print 'Got requests'

    UP = price2 - PRE_price
    bot.sendMessage(1061745573, 'Bithumb-BTC-KRW: '+str(price2)+', UP: '+str(UP))
    PRE_price = price2

sched = BlockingScheduler()

# Schedule save_price to be called every minuates.
sched.add_job(write_price, 'interval', seconds = 60, id='print_price_id')

sched.start()
