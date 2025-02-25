from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException
import time

# Initialize WebDriver
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://demoblaze.com")

try:
    try:
        nav_login = driver.find_element(By.ID, "login2")
        nav_login.click()
        time.sleep(2)  # Wait for modal to appear
    except NoSuchElementException as e:
        print("Login button not found:", e)
        raise e

    try:
        uname = driver.find_element(By.ID, "loginusername")
        uname.send_keys("testmorning")
    except NoSuchElementException as e:
        print("Username field not found:", e)
        raise e

    try:
        pwd = driver.find_element(By.ID, "loginpassword")
        pwd.send_keys("test123")
    except NoSuchElementException as e:
        print("Password field not found:", e)
        raise e

    try:
        loginbutton = driver.find_element(By.XPATH, "//*[@id='logInModal']/div/div/div[3]/button[2]")
        loginbutton.click()
    except NoSuchElementException as e:
        print("Login button inside modal not found:", e)
        raise e

except ElementNotInteractableException as e:
    print("Element not interactable:", e)
except Exception as e:
    print("An unexpected error occurred:", e)
finally:
    driver.quit()  # Ensure the browser closes