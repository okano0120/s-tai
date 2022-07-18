from fetcher import Fetcher

class TestFetcher(Fetcher):
  def __init__(self, settings):
    self.settings = settings

  def fetch(self):
    print('test fetcher')
