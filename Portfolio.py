import numpy as np
import pandas as pd
import Order 
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
        if order.price * order.shares <= self.portfolioCash:
            self.portfolioCash -= order.price * order.shares 
            return True
        return False