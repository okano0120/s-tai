class Fetcher:
  def fetch(self):
    raise NotImplementedError()

class HtmlFetcher(Fetcher):
  def fetch(self):
    print('html fetcher')

class JsonFetcher(Fetcher):
  def fetch(self):
    print('json fetcher')

class TestFetcher(Fetcher):
  def fetch(self):
    print('test fetcher')
