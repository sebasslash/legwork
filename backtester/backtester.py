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
        self.order_book = []
    
    def process_market_event(self, counter):
        for stock in self.market_data.items():
            data_point = stock[1].iloc[counter]
            tick = Tick(
                data_point['open'],
                data_point['high'],
                data_point['low'],
                data_point['close'],
                data_point['volume'],
                stock[0]
            )
            self.market_event_queue.append(tick)
    def print_market_event(self, tick):
        info = tick.get_tick_info()
        print("Processing Event for {} : Details: Open {} High {} Low {} Close {} Volume {}".format(info[0], info[1], info[2], info[3], info[4], info[5]))

    def run(self,step):
        for i in range(step):
            self.process_market_event(i)
            tick = self.market_event_queue.popleft()
            """
                get_tick_info will return a tuple, just so you don't forget
                **Warning messy**
                Tuple follows OHLCV order
                data[0] -> Ticker
                data[1] -> Open 
                data[2] -> High 
                data[3] -> Low 
                data[4] -> Close 
                data[5] -> Volume 
            """
            data = tick.get_tick_info()
            self.print_market_event(tick)
            for j in range(len(self.order_book)):
               if self.order_book[j].ticker == data[0]:
                   if self.order_book[j].has_stop():
                        # TODO TBD
                        print("")
                   elif self.order_book[j].has_limit():
                       if self.order_book[j].limit == data[4] or self.order_book[j].limit == data[1]:
                            # Execute Limit Order
                            print("Has Limit Order")
                   else:
                        # Market Order
                       if data[1] >= data[4]:
                            self.order_book[j].set_executed_price(data[4]) 
                       else:
                            self.order_book[j].set_executed_price(data[1])
                       if self.portfolio.update_portfolio(self.order_book[j]):
                            self.send_fill_notification(self.order_book[j])

    def send_fill_notification(self, order):
        print("ORDER FOR {} FILLED AT {}".format(order.ticker, order.price))

    def backtester_interface(self):
        self.run(10)





