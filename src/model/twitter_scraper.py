import re
import requests

from bs4 import BeautifulSoup

from .scraping_base import ScrapingBase


class TwitterScraper(ScrapingBase):
    def scraping(url: str, ignore=["qiita", "zenn"]):
        gh_trend_page = requests.get(url)

        # Create a BeautifulSoup object
        soup = BeautifulSoup(gh_trend_page.text, "html.parser")
        a_tags = soup.find(
            # TODO: ignore引数に応じて除外条件を設定できるようにする
            "a",
            attrs={"href": re.compile(r"https://twitter.com/[^qiita | ^zenn].+")},
        )
        if a_tags is None:
            return None
        return a_tags.get("href", None)
