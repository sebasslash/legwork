import sys
sys.path.append("..")

from backtester.backtester import *
from backtester.order import *

## This will initialize the backtester, and create your basic portfolio
bt = Backtester()

## TODO: Allow the user to modify their portfolio before the backtester is ran

## Place orders here ##
bt.place_order(Order("AAPL", 50))
bt.place_order(Order("MSFT", 50))

bt.backtester_interface(10)
