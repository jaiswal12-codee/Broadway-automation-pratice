from selenium import webdriver
import time

from selenium.webdriver.common import by
from selenium.webdriver.common.by import By
#open the chrome
driver = webdriver.Chrome()
#maximize the window
driver.maximize_window()
# open the website
driver.get("https://www.demoblaze.com")
#click the  login nav
nav_login= driver.find_element(By.ID,"login2")
nav_login.click()
# live in the page for the 10 second
time.sleep(10)
#  take the id of the textbox and pass value
text_box=driver.find_element(By.ID,"loginusername")
text_box.send_keys("testmorning")
# take the id of password box and send the value
pass_box=driver.find_element(By.ID,"loginpassword")
pass_box.send_keys("test123")
#take the id of the button and click the button
button_1=driver.find_element(By.XPATH,'//*[@id="logInModal"]/div/div/div[3]/button[2]')
button_1.click()
#live in the page for 10 second
time.sleep(10)