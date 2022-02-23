from fetch import Tech
from tweet import Twitter
from model.qiita import QiitaTrend
from model.zenn import ZennTrend
import random

def main():
    # trend = Tech()
    # twitter = Twitter()
    # trend.parse()
    # for message in trend.messages['article']:
    #     twitter.tweet(trend.messages['header'] + "\n" + message + "\n" + "#Qiita" + " #Zenn")
    tech_sites = [
        QiitaTrend(),
        ZennTrend()
    ]
    twitter = Twitter()
    for tech_site in tech_sites:
        trend_results = tech_site.fetch()
        trend = random.choice(trend_results)
        tweet_message_header = f'【今日のトレンド記事のピックアップです！】' + '\n'
        tweet_message_content = list(trend.keys())[0] + "\n" + list(trend.values())[0]
        tweet_message_footer = "#Qiita" + " #Zenn"
        tweet_message = tweet_message_header + "\n" + tweet_message_content + "\n" + tweet_message_footer

        twitter.tweet(tweet_message)
if __name__ == '__main__':
    main()