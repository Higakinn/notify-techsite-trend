
from typing import TypeVar, Dict, List

ArticleTitleType = TypeVar("ArticleTitle", bound=str)
ArticleURLType = TypeVar("ArticleURL", bound=str)

class TechTrendBase:
  def fetch() -> List[Dict[ArticleTitleType, ArticleURLType]]:
    print("トレンド取得")
    raise NotImplementedError()