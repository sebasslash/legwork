
class Auth:
    api_key = ''
    api_secret_key = ''
    api_domain = 'https://api.alpaca.markets/v2'

    def __init__(self, api_key, api_secret_key):
        self.api_key = api_key
        self.api_secret_key = api_secret_key
        
    def get_key(self):
        return self.api_secret_key

    def get_secret_key(self):
        return self.api_secret_key

    def get_api_domain():
        return self.api_domain

    def update(new_api_key, new_api_secret_key):
        self.api_key = new_api_key
        self.api_secret_key = new_api_secret_key