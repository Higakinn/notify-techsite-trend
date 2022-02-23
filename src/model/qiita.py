from urllib import request
import requests
import os

from .tech_trend_base import TechTrendBase


class QiitaTrend(TechTrendBase):
  def __init__(self) -> None:
      self.url = os.getenv(f'TREND_QIITA_URL')
      
  def fetch(self):
      print(f"Qiitaのトレンド記事を取得")
      try :
          response = requests.get(self.url)
      except requests.exceptions.RequestException as e:
          raise SystemExit(e)
      
      results = response.json()
      article_urls = [{article['node']['title']: article['node']['linkUrl']} for article in results]
      return article_urls
      # url = f"{self.service_urls['zenn']}/{article['user']['username']}/articles/{article['slug']}"

