import os
import requests

from bs4 import BeautifulSoup

from .tech_trend_base import TechTrendBase
from lib.translater import translate


# TODO: スクレイピングを定期的に行うのは負荷的よくなさそうなので、別の方法を考える
class DevtoTrend(TechTrendBase):
    def __init__(self) -> None:
        self.url = os.getenv(f"TREND_DEVTO_URL")

    def fetch(self):
        print(f"devtoのトレンド記事を取得")
        devto_base_url = "https://dev.to"
        devto_url = f"{devto_base_url}/top/week"
        print(devto_url)
        devto_top_page = requests.get(devto_url)
        print(devto_top_page)

        soup = BeautifulSoup(devto_top_page.text, "html.parser")
        articles = soup.find_all(
            "a", attrs={"class": "crayons-link crayons-link--contentful"}
        )

        print(articles)

        for article in articles:
            devto_article_url = f"{devto_base_url}{article.get('href')}"
            devto_article_title = article.get_text().splitlines()[1]

        results = []
        for article in articles:
            devto_article_url = f"{devto_base_url}{article.get('href')}"
            devto_article_title = article.get_text().splitlines()[1]
            print("jhh")
            user_name = article.get("href")[1:].split("/")[0]
            user_url = f"{devto_base_url}/{user_name}"
            translated_title_json = translate(devto_article_title)
            title = devto_article_title
            if translated_title_json["code"] == 200:
                title = devto_article_title + "(" + translated_title_json["text"] + ")"

            results.append(
                {"title": title, "url": devto_article_url, "user_url": user_url}
            )
        return results
