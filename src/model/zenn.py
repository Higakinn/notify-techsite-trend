from .tech_trend_base import TechTrendBase
import os
import requests


class ZennTrend(TechTrendBase):
    def __init__(self) -> None:
        self.url = os.getenv(f"TREND_ZENN_URL")

    def fetch(self):
        print(f"zennのトレンド記事を取得")
        try:
            response = requests.get(self.url)
        except requests.exceptions.RequestException as e:
            raise SystemExit(e)

        results = response.json()

        article_urls = []
        zenn_url = "https://zenn.dev"
        for article in results:
            article_slug = article["slug"]
            article_user = article["user"]["username"]
            article_title = article["title"]
            article_user_url = f"{zenn_url}/{article['user']['username']}"
            article_url = f"{zenn_url}/{article_user}/articles/{article_slug}"
            article_urls.append(
                {
                    "title": article_title,
                    "url": article_url,
                    "user_url": article_user_url,
                }
            )

        return article_urls
