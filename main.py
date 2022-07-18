from settings import Settings
from settings import FetcherType
from fetcher import Fetcher
from tracker import Tracker

# print(Settings.interval_second)

class JSONController:
  @classmethod
  def exec(self):
    print('exec')
    settings = Settings('json_tracker', FetcherType.JSON)
    tracker = Tracker(settings)
    tracker.track()

# JSONで取得してくる方法
JSONController.exec()
