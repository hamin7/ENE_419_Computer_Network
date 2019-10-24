import pandas as pd
import requests
import datetime
import matplotlib.pyplot as plt

def price(symbol, comparison_symbols=[''], exchange=''):
    url = 'https://min-api.cryptocompare.com/data/price?fsym={}&tsyms={}'\
        .format(symbol.upper(), ','.join(comparison_symbols).upper())
    if exchange:
        url += '&e={}'.format(exchange)
    page = requests.get(url)
    data = page.json()
    return data

print(price('BTC', ['USD'], exchange='Bitfinex'), price('BTC', ['KRW'], exchange='Bithumb'))
print(price('NEO', ['BTC', 'ETH', 'USD']))