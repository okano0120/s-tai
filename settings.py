from enum import Enum

class FetcherType(Enum):
  HTML = 1
  JSON = 2
  TEST = 3

class Settings:
  def __init__(self, controller_name, fetcher_type):
    # 取得方法は何にするのか
    self.controller_name = controller_name
    self.fetcher_type = fetcher_type

  # === COMMON ===
  # 何秒間隔でリクエストを行うのか(秒)
  interval_second = 10

  # 車のID (String)
  car_number = '244'

  # === JSON Fetcher ===
  # Json APIのSect2SectTimeの順番がどうなっているのか
  sect2_orders = [3, 0, 1, 2]

  # === HTML Fetcher ===
  # テーブルで必要な値 n番目, 0番目始まり
  car_number_order = 2 # TODO: 正しく
  table_orders = [4, 12, 13, 14, 15]
