import numpy as np
import pandas as pd
import matplotlib
from .order import *
from .parser import *
from .portfolio import *
from .tick import *
from collections import deque

class Backtester:
    # This index will record every market tick
    timeIndex = 0

    def __init__(self):
        run_parser()
        self.market_data = get_data()
        self.portfolio = Portfolio()
        self.market_event_queue = deque([])
        self.orderBook = []
    
    def process_market_event(self, counter):
        for ticker in self.market_data.items():
            data_point = self.market_data[ticker].iloc[counter]
            tick = Tick(
                data_point['open'],
                data_point['high'],
                data_point['low'],
                data_point['close'],
                data_point['volume'],
                ticker
            ) 
            self.market_event_queue.append(tick)
    def run(self,step):
        for i in range(step):
            self.process_market_event(i)
            tick = self.market_event_queue.popleft()
            print("Ticker: {} Open")
            for j in range(len(self.orderBook)):
               if self.orderBook[j].ticker == tick.ticker:
                   if self.orderBook[j].has_stop():
                        # TODO TBD
                        print("")
                   elif self.orderBook[j].has_limit():
                       if self.orderBook[j].limit == tick.close or self.orderBook[j].limit == tick.open:
                            # Execute Limit Order
                            print("Has Limit Order")
                   else:
                        # Market Order
                       if tick.open >= tick.close:
                            self.orderBook[j].set_executed_price(tick.close) 
                       else:
                            self.orderBook[j].set_executed_price(tick.open)
                       if self.portfolio.update_portfolio(self.orderBook[j]):
                            self.send_fill_notification(self.orderBook[j])

    def send_fill_notification(self, order):
        print("ORDER FOR {} FILLED AT {}".format(order.ticker, order.price))

    def backtester_interface(self):
        print(next(iter(self.market_data.values())))        





