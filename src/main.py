import random

from tweet import Twitter
from model.qiita import QiitaTrend
from model.zenn import ZennTrend
from model.twitter_scraper import TwitterScraper

# TODO: jinja2で書き換える
def _create_tweet_message(title, url, user):
    tweet_message_header = f"【今日のトレンド記事のピックアップです！】" + "\n"
    tweet_message_content = f"{title}\n{url}\n{user}"
    tweet_message_footer = "#Qiita" + " #Zenn"
    tweet_message = (
        tweet_message_header
        + "\n"
        + tweet_message_content
        + "\n"
        + tweet_message_footer
    )
    return tweet_message


def main():
    tech_sites = [QiitaTrend(), ZennTrend()]
    twitter = Twitter()
    for tech_site in tech_sites:
        try:
            # TODO: 以下5行関数化する

            trend_results = tech_site.fetch()
            trend = random.choice(trend_results)

            twi_url = TwitterScraper.scraping(url=trend["user_url"])
            mention = twi_url.replace("https://twitter.com/", "@")
            tweet_message = _create_tweet_message(trend["title"], trend["url"], mention)

            twitter.tweet(tweet_message)
        except Exception as e:
            # TODO: 以下5行関数化する
            trend = random.choice(trend_results)

            twi_url = TwitterScraper.scraping(url=trend["user_url"])
            if twi_url is None:
                mention = ""
            else:
                mention = twi_url.replace("https://twitter.com/", "@")
            tweet_message = _create_tweet_message(trend["title"], trend["url"], mention)

            twitter.tweet(tweet_message)


if __name__ == "__main__":
    main()
