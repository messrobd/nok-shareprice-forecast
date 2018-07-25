import random
import requests
import os
import json
from matplotlib import pyplot

def get_stock_data(symbol):
    #data provided by alpha vantage API. last 100 days returned by default
    url_base = 'https://www.alphavantage.co/query'
    API_key = 'SYDT0ACA1X9YPHOM'
    payload = {
      'function': 'TIME_SERIES_DAILY',
      'symbol': symbol,
      'apikey': API_key
    }
    response = requests.get(url_base, params=payload)
    return response.json()

def get_FX_data(currency, date):
    #data provided by currencylayer API. non-USD-based rates cost money
    url_base = 'http://apilayer.net/api/historical'
    API_key = '30066134cd1ff0a3811c03fd1b12f307'
    payload = {
      'access_key': API_key,
      'date': date,
      'currencies': currency
    }
    response = requests.get(url_base, params=payload)
    return response.json()

def make_cache_path():
    directory = os.path.dirname(__file__)
    return directory + '/' + 'cache'

def write_cache_file(data):
    full_path = make_cache_path()
    cache_file = open(full_path, 'w')
    json.dump(data, cache_file)
    cache_file.close()

def read_cache_file():
    full_path = make_cache_path()
    cache_file = open(full_path)
    data =  json.load(cache_file)
    cache_file.close()
    return data

def calc_nok_net_return(net_proceeds_usd, usd_to_nok_market, commission):
    return net_proceeds_usd * usd_to_nok_market * (1 - commission)

def calc_net_proceeds_usd(number, fmv_usd):
    gross_proceeds = number * fmv_usd
    trading_fee = gross_proceeds * 0.0075 + 0.30
    wire_fee = 15
    other_fees = gross_proceeds * 0.0008 + 10.017
    return gross_proceeds - trading_fee - wire_fee - other_fees

def random_range_returns(number, fmv_usd_lo, fmv_usd_hi, usd_to_nok_market_lo, usd_to_nok_market_hi, commission):
    fmv_range = []
    returns_range = []
    for i in range(0, 200):
        fmv_usd_scenario = random.uniform(fmv_usd_lo,fmv_usd_hi)
        usd_to_nok_scenario = random.uniform(usd_to_nok_market_lo, usd_to_nok_market_hi)
        net_proceeds_usd = calc_net_proceeds_usd(number, fmv_usd_scenario)
        net_proceeds_nok = calc_nok_net_return(net_proceeds_usd, usd_to_nok_scenario, commission)
        fmv_range.append(fmv_usd_scenario)
        returns_range.append(net_proceeds_nok)
    return fmv_range, returns_range

def calc_range_returns(symbol, number, currency, commission, cache=False):
    raw_stock_data = get_stock_data(symbol)['Time Series (Daily)']
    fmv_range, returns_range = [], []
    for date in raw_stock_data:
        fmv_usd = float(raw_stock_data[date]['4. close'])
        usd_to_nok_market = get_FX_data(currency, date)['quotes']['USD' + currency]
        net_proceeds_usd = calc_net_proceeds_usd(number, fmv_usd)
        net_proceeds_nok = calc_nok_net_return(net_proceeds_usd, usd_to_nok_market, commission)
        fmv_range.append(fmv_usd)
        returns_range.append(net_proceeds_nok)
    if cache:
        data = {}
        data['fmv_usd'] = fmv_range
        data['returns_range'] = returns_range
        write_cache_file(data)
    else:
        return fmv_range, returns_range

def scatter_plot(x_range, y_range, mask):
    pyplot.scatter(x_range, y_range)
    pyplot.plot([min(x_range), max(x_range)], [mask, mask])
    pyplot.show()
