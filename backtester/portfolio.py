import numpy as np
import pandas as pd
from .order import *
class Portfolio:
   def __init__(self):
        self.portfolioValue = 100000
        self.portfolioCash = 100000
        self.marginAmount = 2500
        self.securities = dict() # Ticker -> [Entry Price, Current Price]
        self.short_securities = dict()
    
   def add_security(self, ticker, data, type="long"):
        # TODO
         if type == "long":
               self.securities[ticker] = data
         elif type == "short":
               self.short_securities[ticker] = data             

   def remove_security(self, ticker, type="long"):
         if type == "long":
              del self.securities[ticker]
         elif type == "short":
              del self.short_securities[ticker]
    
   def calculate_performance(self):
        # TODO
        self.portfolioValue = self.portfolioCash
        for security_data in self.securities.items():
            self.portfolioValue += security_data[1]
        print("Portfolio Value: {}".format(self.portfolioValue))
    
   def update_portfolio(self, order):
        price = order.get_order_price()
        shares = order.get_order_shares()
        if price * shares <= self.portfolioCash:
            self.portfolioCash -= price * shares 
            self.add_security(order.get_order_ticker(), {"price": price, "shares": shares})
            return True
        return False