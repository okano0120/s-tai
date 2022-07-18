from html_fetcher import HtmlFetcher
from settings import FetcherType

class Tracker:
  def __init__(self, settings):
    self.settings = settings
    self.last_lap = 0

  def track(self):
    if self.settings.fetcher_type == FetcherType.HTML:
      print('FetcherType.HTML')
