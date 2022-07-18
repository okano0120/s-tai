from settings import Settings
from settings import FetcherType
from fetcher import Fetcher
from tracker import Tracker

# print(Settings.interval_second)

class JSONController:
  @classmethod
  def exec(self):
    settings = Settings('json_tracker', FetcherType.HTML) # TODO: fix json
    tracker = Tracker(settings)
    tracker.track()

# JSONで取得してくる方法
JSONController.exec()
