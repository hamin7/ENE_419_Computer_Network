import requests
import datetime

from apscheduler.schedulers.background import BlockingScheduler

count = 0

Bitfinex_BTC_USD_url = "https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD&e=Bitfinex"
Bithumb_BTC_KRW_url = "https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=KRW&e=Bithumb"

response1 = requests.get(Bitfinex_BTC_USD_url)
response2 = requests.get(Bithumb_BTC_KRW_url)

def print_price():
    global count

    print(datetime.datetime.now(), response1.text, response2.text)

    # execute the job till the count of 5
    count = count + 1
    if count == 5:
        sched.remove_job('print_price_id')

def price(symbol, comparison_symbols=[''], exchange=''):
    url = 'https://min-api.cryptocompare.com/data/price?fsym={}&tsyms={}'\
        .format(symbol.upper(), ','.join(comparison_symbols).upper())
    if exchange:
        url += '&e={}'.format(exchange)
    page = requests.get(url)
    data = page.json()
    return data

sched = BlockingScheduler()

# Schedule print_price to be called every minuates.
sched.add_job(print_price, 'interval', seconds = 2, id='print_price_id')

sched.start()