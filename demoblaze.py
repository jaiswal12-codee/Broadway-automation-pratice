import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.webdriver import Options


class DemoblazeTest(unittest.TestCase):

    def setUp(self):

        self.driver = webdriver.Chrome()
        self.driver.get("https://demoblaze.com")

    def test_login(self):
        driver = self.driver

        # Click on login button
        nav_login = driver.find_element(By.ID, "login2")
        nav_login.click()

        # Wait for login modal
        time.sleep(2)

        # Enter credentials
        uname = driver.find_element(By.ID, "loginusername")
        uname.send_keys("testmorning")

        pwd = driver.find_element(By.ID, "loginpassword")
        pwd.send_keys("test123")

        loginbutton = driver.find_element(By.XPATH, "//*[@id='logInModal']/div/div/div[3]/button[2]")
        loginbutton.click()

        # Wait for login to process
        time.sleep(3)

        # Verify login
        try:
            actual_result = driver.find_element(By.ID, "nameofuser").text
            expected_result = "Welcome testmornig"
            self.assertEqual(actual_result, expected_result, "Login test failed")
        except Exception as e:
            print(e)
            self.fail("Exception occurred while verifying login")

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
