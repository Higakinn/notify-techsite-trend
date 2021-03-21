import requests
import os
from pprint import pprint 

class Tech():
    def __init__(self):
        self.urls = {
            'zenn': os.getenv('TREND_ZENN_URL'),
            'qiita': os.getenv('TREND_QIITA_URL')
        }

    def get_trend(self, service='zenn'):
        try :
            response = requests.get(self.urls[service])
        except requests.exceptions.RequestException as e:
            raise SystemExit(e)
        
        return response.json()
    
    def parse(self):
        # それぞれのトレンド情報をparseする
        for service in self.urls.keys():
            pprint(self.get_trend(service))
        
