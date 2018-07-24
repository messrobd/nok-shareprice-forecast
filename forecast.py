import random
from matplotlib.pyplot import *

def calc_nok_net_return(net_proceeds_usd, usd_to_nok_market, commission):
    return net_proceeds_usd / (usd_to_nok_market * (1 - commission))

def calc_net_proceeds_usd(number, fmv_usd):
    gross_proceeds = number * fmv_usd
    trading_fee = gross_proceeds * 0.0075 + 0.30
    wire_fee = 15
    other_fees = gross_proceeds * 0.0008 + 10.017
    return gross_proceeds - trading_fee - wire_fee - other_fees

def calc_range_returns(number, fmv_usd_lo, fmv_usd_hi, usd_to_nok_market_lo, usd_to_nok_market_hi, commission):
    fmv_range = []
    returns_range = []
    for i in range(0, 10):
        fmv_usd_scenario = random.uniform(fmv_usd_lo,fmv_usd_hi)
        usd_to_nok_scenario = random.uniform(usd_to_nok_market_lo, usd_to_nok_market_hi)
        net_proceeds_usd = calc_net_proceeds_usd(number, fmv_usd_scenario)
        net_proceeds_nok = calc_nok_net_return(net_proceeds_usd, usd_to_nok_scenario, commission)
        fmv_range.append(fmv_usd_scenario)
        returns_range.append(net_proceeds_nok)
    return fmv_range, returns_range
