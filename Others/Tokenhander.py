import utility.enhance.Sender
from Settings import cofig
import requests
class tokenMamagement:
    def __init__(self):
        self.version =0.1

    @staticmethod
    def get_token(url,params):
        get_token=requests.post(url,params)
        return get_token





