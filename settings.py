from enum import Enum

class FetcherType(Enum):
  HTML = 1
  JSON = 2
  TEST = 3

class Settings:
  # === COMMON ===
  # 何秒間隔でリクエストを行うのか(秒)
  interval_second = 10

  # 車のID (String)
  car_number = '244'

  # 取得中に取得内容を出力するかどうか (Trueの場合: する)
  is_display_fetcher_data = True

  # === JSON Fetcher ===
  json_fetcher = {
    # Json APIのSect2SectTimeの順番がどうなっているのか
    'sect2_orders': [3, 0, 1, 2]
  }

  # === HTML Fetcher ===
  html_fetcher = {
    # テーブルにおける車のIDの順番 n番目, 0番目始まり
    'car_number_order': 2, # TODO: 正しく

    # テーブルにおける取得するデータの順番 n番目, 0番目始まり
    'table_orders': [4, 12, 13, 14, 15]
  }

  # === TEST Fetcher ===
  test_fetcher = {
  }

  # __init__で指定するインスタンスメソッドをコントローラーから指定するため、手動で書き換えない
  def __init__(self, controller_name, fetcher_type):
    # コントローラー名 (csv出力時に利用する)
    self.controller_name = controller_name

    # 取得方法は何にするのか
    self.fetcher_type = fetcher_type
