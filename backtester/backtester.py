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
        """
            stock[0] -> Stock's ticker
            stock[1] -> Stock's dataframe
        """
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

    def run(self,step, print=False):
        previous_tick = None 
        for i in range(step):
            self.pre_market(previous_tick)
            self.process_market_event(i)
            tick = self.market_event_queue.popleft()
            previous_tick = tick
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
            self.during_market(tick)
            if print:
                self.print_market_event(tick)
            for j in range(len(self.order_book)):
               if self.order_book[j].get_order_ticker() == data[0]:
                   if self.order_book[j].has_stop():
                        # TODO TBD
                        print("Has Stop")
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
                    #    del self.order_book[j]
                   else:
                       print("Order for : {} @ {} for {} shares can not be fulfilled, lack of available funds"
                                                    .format(self.order_book[j].get_order_ticker(), 
                                                            self.order_book[j].get_order_price(),
                                                            self.order_book[j].get_order_shares()))
                       
            # Remove any filled orders
            self.order_book = [order for order in self.order_book if not order.get_order_filled()]
            self.post_market(tick)



    def place_order(self, order):
        self.order_book.append(order) 
    def send_fill_notification(self, order):
        print("ORDER FOR {} FILLED @ {}".format(order.ticker, order.price))
        order.set_filled(True)

    def get_market_data(self):
        data = []
        for stock in self.market_data.items():
            data.append(stock[1])
        return data
    def backtester_interface(self, iterations, pre_market, during_market, post_market, flags=None):
        self.pre_market = pre_market
        self.during_market = during_market
        self.post_market = post_market
        if flags is not None and "print" in flags:
            self.run(iterations, True)
        else:
            self.run(iterations)





