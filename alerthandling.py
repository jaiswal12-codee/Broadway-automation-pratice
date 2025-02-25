import time
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common.by import By
from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://demo.automationtesting.in/Alerts.html")
simpleNav = driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div[1]/ul/li[1]/a')
simpleNav.click()
button1 = driver.find_element(By.XPATH,'//*[@id=\"OKTab\"]/button')
button1.click()
time.sleep(10)
art = driver.switch_to.alert
art.accept()
confirmNav = driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div[1]/ul/li[2]/a')
confirmNav.click()
button2 = driver.find_element(By.XPATH,'//*[@id=\"CancelTab\"]/button')
button2.click()
time.sleep(10)
art.dismiss()

textBoxNav = driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div[1]/ul/li[3]/a')
textBoxNav.click()
button3 = driver.find_element(By.XPATH,'//*[@id=\"Textbox\"]/button')
button3.click()
time.sleep(10)
art.send_keys("qaclass")
art.accept()