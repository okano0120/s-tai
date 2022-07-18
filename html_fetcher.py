from fetcher import Fetcher
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

class HtmlFetcher(Fetcher):
  def __init__(self):
    site_url = "https://www.supertaikyu.live/timings/" 
    self.driver = webdriver.Chrome(ChromeDriverManager().install())
    self.driver.get(site_url);

  def fetch(self):
    table = self.driver.find_element("id", "timing_table")
    print(table)
