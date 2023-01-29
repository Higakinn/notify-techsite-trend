import tweepy
import os
import time


class Twitter:
    def __init__(self):
        client_key = os.getenv("TWITTER_API_KEY")
        client_secret = os.getenv("TWITTER_API_SECRET_KEY")
        access_token = os.getenv("TWITTER_ACCESS_TOKEN")
        access_token_secret = os.getenv("TWITTER_ACCESS_TOKEN_SECRET")
        auth = tweepy.OAuthHandler(client_key, client_secret)
        auth.set_access_token(access_token, access_token_secret)
        self.api = tweepy.API(auth)

    def tweet(self, message=time.time()):  # 好きな言葉をツイート
        status = self.api.update_status(message)
        return status.id

    def reply(self, tweet_id, message=time.time()):
        self.api.update_status(message, in_reply_to_status_id=tweet_id)
        print(f"リプライ!")
