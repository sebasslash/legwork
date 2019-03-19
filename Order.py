import numpy as np
import pandas as pd

class Order:
    id = 0
    def __init__(self, ticker, num_of_shares, stop=None, limit=None):
       self.ticker = ticker
       self.shares = num_of_shares
       self.stop = stop
       self.limit = limit
       Order.id += 1
    
    def get_order_information(self, id):
       return self.ticker, self.price, self.shares, self.stop, self.limit
    
    def update_order(self, num_of_shares):
       self.shares += num_of_shares
    
    def update_limit_order(self, new_limit):
       self.limit = new_limit
    
    def update_stop_order(self, new_stop):
       self.stop = new_stop
    def set_executed_price(self, price):
        self.price = price
