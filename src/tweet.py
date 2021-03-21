import tweepy
import os
import time

class Twitter():
    def __init__(self):
        client_key = os.getenv('TWITTER_API_KEY')
        client_secret = os.getenv('TWITTER_API_SECRET_KEY')
        access_token = os.getenv('TWITTER_ACCESS_TOKEN')
        access_token_secret = os.getenv('TWITTER_ACCESS_TOKEN_SECRET')
        auth = tweepy.OAuthHandler(client_key, client_secret)
        auth.set_access_token(access_token, access_token_secret)
        self.api = tweepy.API(auth)

    def tweet(self, message=time.time()): # 好きな言葉をツイート
        self.api.update_status(message)
