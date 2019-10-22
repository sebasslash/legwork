from .auth import *
import requests as rq
class Account:
    def __init__(self, api_key, secret_api_key):
        self.auth = Auth(api_key, secret_api_key) 
        self.account = self.query_account(self.auth)
        self.headers = {
            'APCA-API-KEY-ID': self.auth.get_key(),
            'APCA-API-SECRET-KEY': self.auth.get_secret_key()
        }
    def get_buying_power(self):
        return self.account.buying_power

    def get_cash(self):
        return self.account.cash

    def get_equity(self):
        return self.account.equity 

    def get_credentials(self):
        return self.headers
    
    def get_domain(self):
        return self.auth.get_api_domain()
    
    def get_initial_margin(self):
        return self.account.initial_margin

    def get_last_margin(self):
        return self.account.last_maintenance_margin

    def update_account_info(self):
        self.account = self.query_account(self.auth)

    def get_all_orders(self):
        return rq.get(self.auth.get_api_domain() + '/orders', headers=self.headers)
    
    def get_order_by(self, status='all', limit='50', after=None, until=None, direction='desc'):
        params = {
            'status': status,
            'limit': limit,
            'after': after,
            'until': until,
        }
        return rq.get(self.auth.get_api_domain() + '/orders', headers=self.headers, params=params)

    def update_account_auth(self, auth):
        self.auth = auth
    
    def get_account(self):
        return self.account

    def query_account(self, auth):
        return rq.get(self.auth.get_api_domain() + '/account', headers=self.headers)
