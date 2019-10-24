import requests
import datetime
import json, ast
import pandas as pd
import csv

from apscheduler.schedulers.background import BlockingScheduler

# function that print the price
def print_price():
    now = datetime.datetime.now()
    nowDatetime = now.strftime('%Y-%m-%d %H:%M:%S')
    
    price1 = ast.literal_eval(json.dumps(price('BTC', ['USD'], exchange='Bitfinex')))
    price2 = ast.literal_eval(json.dumps(price('BTC', ['KRW'], exchange='Bithumb')))

    print(nowDatetime, price1, price2)

#function that Get the price
def price(symbol, comparison_symbols=[''], exchange=''):
    url = 'https://min-api.cryptocompare.com/data/price?fsym={}&tsyms={}'\
        .format(symbol.upper(), ','.join(comparison_symbols).upper())
    if exchange:
        url += '&e={}'.format(exchange)
    page = requests.get(url)
    data = page.json()
    return data

def save_price():
    now = datetime.datetime.now()
    nowDatetime = now.strftime('%Y-%m-%d %H:%M:%S')
    
    price1 = ast.literal_eval(json.dumps(price('BTC', ['USD'], exchange='Bitfinex')))
    price2 = ast.literal_eval(json.dumps(price('BTC', ['KRW'], exchange='Bithumb')))
    
    # data = [[nowDatetime, price1, price2]]

    adding_dataframe = pd.DataFrame(
        {"Datetime": nowDatetime, "Bitfinex_USD": price1, "Bithumb": price2}
    )
    adding_dataframe.to_csv("./data/BitCoin.csv")
    print(adding_dataframe[:20])
    # dataframe.to_csv("/Users/hamin/newapp/BitCoin.csv", header=False, index=False)

def write_spam():
    with open('BitCoin.csv', 'wb') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        spamwriter.writerow(['spam'] * 5 + ['Baked Beans'])
        spamwriter.writerow(['span', 'Lovely Span', 'Wonderful Spam'])

def write_spam1():
    with open('BitCoin.csv', 'w') as csvfile:
        fieldnames = ['first_name', 'last_name']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerow({'first_name': 'Baked', 'last_name': 'Beans'})
        writer.writerow({'first_name': 'Lovely', 'last_name': 'Spam'})
        writer.writerow({'first_name': 'Wonderful', 'last_name': 'Spam'})

def write_price():
    now = datetime.datetime.now()
    nowDatetime = now.strftime('%Y-%m-%d %H:%M:%S')

    price1 = ast.literal_eval(json.dumps(price('BTC', ['USD'], exchange='Bitfinex')))
    price2 = ast.literal_eval(json.dumps(price('BTC', ['KRW'], exchange='Bithumb')))

    with open('BitCoin.csv', 'w') as csvfile:
        fieldnames = ['Date', 'Bitfinex-USD', 'Bithum-KRW']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerow({'Date': nowDatetime, 'Bithum-KRW': price1, 'Bitfinex-USD': price2})
        writer.writerow({'Date': nowDatetime, 'Bithum-KRW': price1, 'Bitfinex-USD': price2})
        writer.writerow({'Date': nowDatetime, 'Bithum-KRW': price1, 'Bitfinex-USD': price2})

sched = BlockingScheduler()

# Schedule print_price to be called every minuates.
#sched.add_job(print_price, 'interval', seconds = 2, id='print_price_id')

# Schedule save_price to be called every minuates.
#sched.add_job(save_price, 'interval', seconds = 2, id='print_price_id')

# Schedule save_spam to be called every minuates.
#sched.add_job(write_spam, 'interval', seconds = 2, id='print_price_id')

# Schedule save_price to be called every minuates.
#sched.add_job(write_spam1, 'interval', seconds = 2, id='print_price_id')

# Schedule save_price to be called every minuates.
sched.add_job(write_price, 'interval', seconds = 2, id='print_price_id')

sched.start()

write_price()