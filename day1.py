import time

from selenium  import webdriver
#open the  chrome in webdriver and store the value in driver
driver =webdriver.Chrome()
#maximize the window
driver.maximize_window()
# open the url
driver.get("https://www.demoblaze.com")
#wait for 10 second
time.sleep(10)
