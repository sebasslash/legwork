import sys
sys.path.append("..")

from backtester.backtester import *
from backtester.order import *
from backtester.indicators.sma import *

## This will initialize the backtester, and create your basic portfolio
bt = Backtester()

market_data  = bt.get_market_data()

## TODO: Allow the user to modify their portfolio before the backtester is ran

sma = SMA(market_data[0], 5)
## Place orders here ##
def pre_market(tick):
    bt.place_order(Order("AAPL", 50))
    bt.place_order(Order("MSFT", 50))

def during_market(tick):
    print("Ticker: " + str(tick.ticker) + " Open: " + str(tick.open))

def post_market(tick):
    print("Ticker: " + str(tick.ticker) + " Close: " + str(tick.close))

bt.backtester_interface(10, pre_market, during_market, post_market)
