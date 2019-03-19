class Tick:
    def __init__(self, o, h, l, c, v, ticker):
        self.open   = o 
        self.high   = h 
        self.low    = l 
        self.close  = c 
        self.volume = v 
        self.ticker = ticker
    def get_ticker(self):
        return self.ticker

