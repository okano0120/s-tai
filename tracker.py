from html_fetcher import HtmlFetcher
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
      return HtmlFetcher() # TODO: change
    elif fetcher_type == FetcherType.TEST:
      return HtmlFetcher() # TODO: change
    else:
      raise ValueError("正しいFetcherを指定してください")

  def track(self):
    self.fetcher.fetch()
