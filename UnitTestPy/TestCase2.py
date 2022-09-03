import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

class SearchEnginesTest(unittest.TestCase):
    def test_Google(self):
        # initialize chrome driver manager
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("https://www.google.com/")
        print("the title of page is ", self.driver.title)
        time.sleep(5)
        self.driver.close()

    def test_Bing(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("https://www.bing.com")
        print("The title of page is " , self.driver.title)
        time.sleep(5)
        self.driver.close()

if __name__ == "__main__":
    unittest.main()