from tweet import Twitter
from model.qiita import QiitaTrend
from model.zenn import ZennTrend
import random

def _create_tweet_message(title, url):
    tweet_message_header = f'【今日のトレンド記事のピックアップです！】' + '\n'
    tweet_message_content = title + "\n" + url
    tweet_message_footer = "#Qiita" + " #Zenn"
    tweet_message = tweet_message_header + "\n" + tweet_message_content + "\n" + tweet_message_footer
    return tweet_message

def main():
    tech_sites = [
        QiitaTrend(),
        ZennTrend()
    ]
    twitter = Twitter()
    for tech_site in tech_sites:
        try:
            trend_results = tech_site.fetch()

            trend = random.choice(trend_results)
            tweet_message = _create_tweet_message(trend['title'], trend['url'])

            twitter.tweet(tweet_message)    
        except Exception as e:
            trend = random.choice(trend_results)
            tweet_message = _create_tweet_message(trend['title'], trend['url'])

            twitter.tweet(tweet_message)    


if __name__ == '__main__':
    main()