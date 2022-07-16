# import requests
import inspect
import json
# from bs4 import BeautifulSoup
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

import time

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get("https://www.supertaikyu.live/timings/");

# element = driver.find_element_by_css_selector('#timing_table')

time.sleep(3)
t = driver.find_element("id", "timing_table")
tr = t.find_elements(By.TAG_NAME, 'tr')

# print(tr[0].text)
# print(tr[1].text)

print(type(tr))

# for x in inspect.getmembers(driver, inspect.ismethod):
#   print(x[0])
# # print(element)

# html_text = requests.get('https://www.supertaikyu.live/timings/').text
# soup = BeautifulSoup(html_text, 'html.parser')

# print(soup.select("#timing_table")	)
