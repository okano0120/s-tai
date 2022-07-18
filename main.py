# === USAGE ===
# 1. settings.pyの内容が正しいかどうか確認する
# 
# 2. 実行する (実行方法は下記の3通りtoori)
# - $ python main.py <- JSONを利用してデータを取得する
# - $ python main.py html <- HTMLを利用してデータを取得する
# - $ python main.py test <- テストデータを利用してデータを取得する (デバッグ用)

import sys
from settings import Settings
from settings import FetcherType
from fetcher import Fetcher
from tracker import Tracker
from test_fetcher import TestPattern
from test_fetcher import TestFetcher

class BaseController:
  @classmethod
  def exec(self, settings):
    tracker = Tracker(settings)
    tracker.track()

class JsonController(BaseController):
  @classmethod
  def exec(self):
    settings = Settings('json_tracker', FetcherType.JSON)
    super().exec(settings)

class HtmlController(BaseController):
  @classmethod
  def exec(self):
    settings = Settings('html_tracker', FetcherType.HTML)
    super().exec(settings)

class TestController(BaseController):
  @classmethod
  def exec(self):
    settings = Settings('test_tracker', FetcherType.TEST)
    settings.interval_second = 0.5
    settings.retry_count_limit = 1

    TestFetcher.test_pattern = TestPattern.NORMAL
    super().exec(settings)

controller_class = None
if sys.argv[-1] == 'html':
  controller_class = HtmlController
elif sys.argv[-1] == 'test':
  controller_class = TestController
else:
  controller_class = JsonController

controller_class.exec()
