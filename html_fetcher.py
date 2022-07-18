from fetcher import Fetcher
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

class HtmlFetcher(Fetcher):
  def fetch(self):
    print('html fetcher')
