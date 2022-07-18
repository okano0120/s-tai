class Fetcher:
  def fetch(self):
    raise NotImplementedError()

class JsonFetcher(Fetcher):
  def fetch(self):
    print('json fetcher')

class TestFetcher(Fetcher):
  def fetch(self):
    print('test fetcher')
