import re
import requests

from bs4 import BeautifulSoup

from .scraping_base import ScrapingBase


class TwitterScraper(ScrapingBase):
    def scraping(url: str, ignore="qiita"):
        gh_trend_page = requests.get(url)

        # Create a BeautifulSoup object
        soup = BeautifulSoup(gh_trend_page.text, "html.parser")
        a_tags = soup.find(
            "a",
            attrs={"href": eval(f"_{ignore}_recomplie")()},
        )
        if a_tags is None:
            return None
        return a_tags.get("href", None)


def _qiita_recomplie():
    return re.compile(r"https://twitter.com/[^qiita].+")


def _zenn_recomplie():
    return re.compile(r"https://twitter.com/[^zenn].+")


def _devto_recomplie():
    return re.compile(r"https://twitter.com/[^thepracticaldev].+")
