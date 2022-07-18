import requests
from fetcher import Fetcher

class JsonFetcher(Fetcher):
  def __init__(self, car_number, settings):
    self.car_number = car_number
    self.settings = settings
    self.json_url = 'https://www.supertaikyu.live/json/livemoni.json'

  def fetch(self):
    sect2_orders = self.settings['sect2_orders']
    livemoni = requests.get(self.json_url)
    car_timings = livemoni.json()['LiveData']

    record = []

    for car_timing in car_timings:
      if car_timing['CarNo'] == self.car_number:
        times = car_timing['Sect2SectTime']
        record.append(car_timing['LAPS'])

        for sect2_order in sect2_orders:
          record.append(str(times[sect2_order] / 1000))

    return record
