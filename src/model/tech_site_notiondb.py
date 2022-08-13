import os

from lib.notion_client import insert_into_db


class TechSiteNotionDB:
    def __init__(self):
        self.token = os.getenv("NOTION_API_TOKEN")
        self.database_id = os.getenv("NOTION_DB")

    def insert(self, title, site_name, url, user_url, twitter_url):
        notion_properties = {
            "title": {
                "title": [
                    {"text": {"content": title}},
                ]
            },
            "site_name": {"multi_select": [{"name": site_name}]},
            "url": {"url": url},
            "user_url": {"url": user_url},
            "twitter_url": {"url": twitter_url},
        }
        insert_into_db(self.token, self.database_id, notion_properties)
