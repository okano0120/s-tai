from html_fetcher import HtmlFetcher
from json_fetcher import JsonFetcher
from test_fetcher import TestFetcher
from settings import FetcherType
import time

class Tracker:
  def __init__(self, settings):
    self.settings = settings
    self.last_lap = 0
    self.retry_count = 0
    self.fetcher = self.selectFetcher(settings.fetcher_type)

  def selectFetcher(self, fetcher_type):
    car_number = self.settings.car_number
    if fetcher_type == FetcherType.HTML:
      return HtmlFetcher(car_number, self.settings.html_fetcher)
    elif fetcher_type == FetcherType.JSON:
      return JsonFetcher(car_number, self.settings.json_fetcher)
    elif fetcher_type == FetcherType.TEST:
      return TestFetcher(self.settings.test_fetcher)
    else:
      raise ValueError("正しいFetcherを指定してください")

  def track(self):
    while(True):
      time.sleep(self.settings.interval_second)
      try:
        record = self.fetcher.fetch()
        self.retry_count = 0
      except:
        if self.settings.retry_count_limit - 1 <= self.retry_count:
          print('エラーが発生しました。また、リトライ上限に達したためシステムを終了します')
          break

        self.retry_count += 1
        print('エラーが発生しました。Retryします')

      print(record)
