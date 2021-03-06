from forecast import *

number = 93
symbol = 'SLB'
currency = 'NOK'
#fmv_usd_lo = fmv_usd = 67.00
#fmv_usd_hi = 70
#usd_to_nok_market_lo = usd_to_nok_market = 0.125
#usd_to_nok_market_hi = 0.12
commission = 0.0
fmv_usd_purchase = 67.43
usd_to_nok_market_purchase = 8.1588
purchase = number * fmv_usd_purchase * usd_to_nok_market_purchase

'''
print calc_net_proceeds_usd(10, fmv_usd)
print random_range_returns(number, fmv_usd_lo, fmv_usd_hi, usd_to_nok_market_lo, usd_to_nok_market_hi, commission)
'''
'''
prices, returns = random_range_returns(number, fmv_usd_lo, fmv_usd_hi, usd_to_nok_market_lo, usd_to_nok_market_hi, commission)

scatter_plot(prices, returns, purchase)
'''

#make_price_dataset(symbol, currency, True)
dataset = read_cache_file()
prices, returns = calc_range_returns(dataset, number, commission)

scatter_plot(prices, returns, purchase)
