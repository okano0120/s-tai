from fetcher import Fetcher

class JsonFetcher(Fetcher):
  def __init__(self, settings):
    self.settings = settings

  def fetch(self):
    print('json fetcher')
