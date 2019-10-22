import requests as rq
class Order:

    def __init__(self, account, symbol, qty=100, side='buy', 
    type='market', time_in_force='gtc', limit_price=None, stop_price=None, extended_hours=False):
        self.account = account 
        self.symbol = symbol
        self.qty = qty 
        self.side = side 
        self.type = type 
        self.time_in_force = time_in_force 
        self.limit_price = limit_price
        self.stop_price = stop_price
        self.extended_hours = extended_hours
    # TODO: Modify/Get Order Details

    def place_order(self):
        if self.limit_price is None:
            self.limit_price = ''
        if self.stop_price is None:
            self.stop_price = ''
        params = {
            'account': self.account,
            'symbol': self.symbol,
            'qty': str(self.qty),
            'side': self.side,
            'type': self.type,
            'time_in_force': self.time_in_force,
            'limit_price': str(self.limit_price),
            'stop_price': str(self.stop_price),
            'extended_hours': str(self.extended_hours)
        }
        rq.post(account.get_domain() + '/orders', headers=self.account.get_credentials, params=params)
        

