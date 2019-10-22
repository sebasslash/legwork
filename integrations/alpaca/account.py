from .auth import *
import requests as rq
class Account:
    def __init__(self, auth):
        self.auth = auth
        self.account = self.query_account(self.auth)
    def get_buying_power(self):
        return self.account.buying_power

    def get_cash(self):
        return self.account.cash

    def get_equity(self):
        return self.account.equity 

    def get_initial_margin(self):
        return self.account.initial_margin

    def get_last_margin(self):
        return self.account.last_maintenance_margin

    def update_account_info(self):
        self.account = self.query_account(self.auth)

    def update_account_auth(self, auth):
        self.auth = auth
    
    def get_full_info(self):
        return self.account

    def query_account(self, auth):
        return rq.get(self.auth.get_api_domain() + '/account', headers= {
            'APCA-API-KEY-ID': self.auth.get_key(),
            'APCA-API-SECRET-KEY': self.auth.get_secret_key()
        })
