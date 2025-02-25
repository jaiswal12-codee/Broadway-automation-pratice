from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


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
ww = WebDriverWait(driver, 10)

# Wait for the username field to be clickable
uname = ww.until(EC.element_to_be_clickable((By.ID, "loginusername")))
uname.send_keys("testmorning")

pass_box=driver.find_element(By.ID,"loginpassword")
pass_box.send_keys("test123")
#take the id of the button and click the button
button_1=driver.find_element(By.XPATH,'//*[@id="logInModal"]/div/div/div[3]/button[2]')
button_1.click()

