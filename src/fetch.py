import requests
import random
import os
from pprint import pprint 

class Tech():
    def __init__(self):
        self.urls = {
            'zenn': os.getenv('TREND_ZENN_URL'),
            'qiita': os.getenv('TREND_QIITA_URL')
        }
        self.service_urls = {
            'zenn': 'https://zenn.dev',
            'qiita': 'https://qiita.com'
        }
        self.TOPICS = ['flutter','go']
        self.messages = {
            'header' : f'【今日のトレンド記事のピックアップです！】' + '\n',
            'article' : []
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
            trend_json_message = self.get_trend(service)
            getattr(self, f"_parse_{service}_random")(trend_json_message)
            #pprint(self.get_trend(service))

    def _parse_zenn_random(self, json):
        article = random.choice(json)
        url = f"{self.service_urls['zenn']}/{article['user']['username']}/articles/{article['slug']}"
        self.messages['article'].append(article["title"] + "\n" + url + "\n")

    def _parse_qiita_random(self, json):
        article = random.choice(json)
        url = article['node']['linkUrl']
        self.messages['article'].append(article['node']['title'] + "\n" + url + "\n")


    def _parse_zenn(self, json):
        print("zenn")
        for article in json: #zennの記事情報からそれぞれの記事を取り出す
            # 各記事のURLを作成
            url = f"{self.service_urls['zenn']}/{article['user']['username']}/articles/{article['slug']}"
            for topic in article['topics']:
                # topicで絞り込み
                if topic['name'].lower() in self.TOPICS:
                    self.messages['article'].append(article["title"] + "\n" + url + "\n")
    
    def _parse_qiita(self, json):
        print("qiita")
        for article in json: #qiitaの記事情報からそれぞれの記事を取り出す
            url = article['node']['linkUrl']
            for topic in article['node']['tags']:
                if topic['name'].lower() in self.TOPICS:
                    self.messages['article'].append(article['node']['title'] + "\n" + url + "\n")
