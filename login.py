from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest

class login(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.get("https://www.demoblaze.com/")
        cls.driver.implicitly_wait(10)

    def test_login(self):
        nav_login = self.driver.find_element(By.ID, "login2")
        nav_login.click()
        text_box = self.driver.find_element(By.ID, "loginusername")
        text_box.send_keys("testmorning")
        pass_box = self.driver.find_element(By.ID, "loginpassword")
        pass_box.send_keys("test123")
        button_1 = self.driver.find_element(By.XPATH, '//*[@id="logInModal"]/div/div/div[3]/button[2]')
        button_1.click()



    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()

    if __name__ == "__main__":
        unittest.main()

