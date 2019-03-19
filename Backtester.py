import parser
import numpy as np
import pandas as pd
import Order 
import Event 
import matplotlib
from .portfolio import Portfolio
from .tick import Tick
import queue

class Backtester:
    # This index will record every market tick
    self.timeIndex = 0

    def __init__(self):
        parser.run_parser()
        self.market_data = parser.get_data()
        self.portfolio = Portfolio()
        self.market_event_queue = queue.Queue()
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
            self.market_event_queue.put(tick)
    def run(step):
        for i in range(step):
            self.process_market_event(i)
            tick = market_event_queue.pop()
            print()
            for j in range(len(self.orderBook)):
               if orderBook[j].ticker == tick.ticker:
                   # TODO
                    if orderBook[j].has_stop():
                        # TODO
                    elif orderBook[j].has_limit():
                        # TODO
                    else:
                        # Market Order
                       orderBook[j].set_executed_price(tick.close) 
                       if self.portfolio.update_portfolio(orderBook[j]):
                            send_fill_notification(orderBook[j])

    def send_fill_notification(order):
        print("ORDER FOR {} FILLED AT {}".format(order.ticker, order.price))

    def backtester_interface():
        





