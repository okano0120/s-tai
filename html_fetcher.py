from fetcher import Fetcher
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

class HtmlFetcher(Fetcher):
  def __init__(self, car_number, settings):
    self.car_number = car_number
    self.settings = settings
    site_url = "https://www.supertaikyu.live/timings/" 

    options = Options()
    options.add_argument('--headless')

    self.driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    self.driver.get(site_url);

  def fetch(self):
    car_number_order = self.settings['car_number_order']
    table_orders = self.settings['table_orders']

    table = self.driver.find_element("id", "timing_table")
    car_timings = table.find_elements(By.TAG_NAME, 'tr')
    car_timings.pop(0) # Table Header削除

    record = []

    for car_timing in car_timings:
      values = car_timing.find_elements(By.TAG_NAME, 'td')
      if values[car_number_order].text == self.car_number:
        for table_order in table_orders:
          record.append(values[table_order].text)

    return record
