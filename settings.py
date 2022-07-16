from enum import Enum

class FetcherType(Enum):
  HTML = 1
  JSON = 2
  TEST = 3

class Settings:
  # 何秒間隔でリクエストを行うのか
  interval_second = 10

  # Json APIのSect2SectTimeの順番がどうなっているのか [only JSON Fetcher]
  sect2_order = [3, 0, 1, 2]

  # テーブルで必要な値 n番目, 0番目始まり [only HTML Fetcher]
  table_order = [4, 12, 13, 14, 15]

  # 取得方法は何にするのか [手動で変更しない]
  fetcher_type = FetcherType.HTML
