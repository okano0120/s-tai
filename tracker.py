from html_fetcher import HtmlFetcher
from json_fetcher import JsonFetcher
from test_fetcher import TestFetcher
from settings import FetcherType

class Tracker:
  def __init__(self, settings):
    self.settings = settings
    self.last_lap = 0
    self.fetcher = self.selectFetcher(settings.fetcher_type)

  def selectFetcher(self, fetcher_type):
    if fetcher_type == FetcherType.HTML:
      return HtmlFetcher()
    elif fetcher_type == FetcherType.JSON:
      return JsonFetcher()
    elif fetcher_type == FetcherType.TEST:
      return TestFetcher()
    else:
      raise ValueError("正しいFetcherを指定してください")

  def track(self):
    self.fetcher.fetch()
