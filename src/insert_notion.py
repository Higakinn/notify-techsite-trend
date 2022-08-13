import time

from tweet import Twitter
from model.qiita import QiitaTrend
from model.zenn import ZennTrend
from model.devto import DevtoTrend
from model.twitter_scraper import TwitterScraper
from model.tech_site_notiondb import TechSiteNotionDB

tech_sites = [
    {"site_name": "qiita", "object": QiitaTrend()},
    {"site_name": "zenn", "object": ZennTrend()},
    {"site_name": "devto", "object": DevtoTrend()},
]

notiondb_client = TechSiteNotionDB()

for tech_site_info in tech_sites:
    try:
        tech_site_name = tech_site_info["site_name"]
        tech_site = tech_site_info["object"]

        trend_results = tech_site.fetch()
        for trend_result in trend_results:
            twi_url = TwitterScraper.scraping(
                url=trend_result["user_url"], ignore=tech_site_name
            )
            notiondb_client.insert(
                title=trend_result["title"],
                site_name=tech_site_name,
                url=trend_result["url"],
                user_url=trend_result["user_url"],
                twitter_url=twi_url or "None",
            )
            time.sleep(0.5)
    except Exception as e:
        print(e)
