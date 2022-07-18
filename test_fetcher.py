from fetcher import Fetcher
from enum import Enum
import csv

class TestPattern(Enum):
  NORMAL = 1

class TestFetcher(Fetcher):
  test_pattern = None

  def __init__(self, settings):
    if TestFetcher.test_pattern == None:
      raise ValueError("no set test pattern")

    self.settings = settings
    self.fetch_count = 0
    self.test_recoerds = self.get_test_recoerds(TestFetcher.test_pattern)

  def get_test_recoerds(self, test_pattern):
    file_path = './test_files/{test_pattern}.csv'.format(test_pattern=test_pattern.name.lower())
    f = open(file_path, 'r', newline="")
    records = list(csv.reader(f))
    f.close()
    return records

  def fetch(self):
    record = self.test_recoerds[self.fetch_count]
    self.fetch_count += 1
    if len(self.test_recoerds) <= self.fetch_count:
      raise ValueError("out lengh")

    return record
