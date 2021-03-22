from fetch import Tech
from tweet import Twitter


def main():
    trend = Tech()
    twitter = Twitter()
    trend.parse()
    for message in trend.messages['article']:
        twitter.tweet(trend.messages['header'] + "\n" + message + "\n" + "#Qiita" + " #Zenn")

if __name__ == '__main__':
    main()