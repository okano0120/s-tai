# === USAGE ===
# $ python main.py - JSONを利用してデータを取得する
# $ python main.py html - HTMLを利用してデータを取得する
# $ python main.py test - テストデータを利用してデータを取得する

import sys
from settings import Settings
from settings import FetcherType
from fetcher import Fetcher
from tracker import Tracker

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
    super().exec(settings)

# JSONで取得してくる方法
# JsonController.exec()

controller_class = None
if sys.argv[-1] == 'html':
  controller_class = HtmlController
elif sys.argv[-1] == 'test':
  controller_class = TestController
else:
  controller_class = JsonController

controller_class.exec()
