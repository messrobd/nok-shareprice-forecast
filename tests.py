from forecast import *

number = 93
fmv_usd_lo = fmv_usd = 67.00
fmv_usd_hi = 70
usd_to_nok_market_lo = usd_to_nok_market = 0.125
usd_to_nok_market_hi = 0.12
commission = 0.02
purchase = number * 67.43 * 8.1588

'''
print calc_net_proceeds_usd(10, fmv_usd)
print calc_range_returns(number, fmv_usd_lo, fmv_usd_hi, usd_to_nok_market_lo, usd_to_nok_market_hi, commission)
'''

prices, returns = calc_range_returns(number, fmv_usd_lo, fmv_usd_hi, usd_to_nok_market_lo, usd_to_nok_market_hi, commission)

scatter_plot(prices, returns, purchase)
