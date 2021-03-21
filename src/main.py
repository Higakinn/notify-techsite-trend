from fetch import Tech
from tweet import Twitter


def main():
    trend = Tech()
    twitter = Twitter()
    trend.parse()
    twitter.tweet()

if __name__ == '__main__':
    main()