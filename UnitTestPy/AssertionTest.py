import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

class Test(unittest.TestCase):
    def testName(self):
        driver  = webdriver.Chrome(ChromeDriverManager().install())
        driver.get('https://www.google.com/')
        titleofWebpage = driver.title

        #assertEqual
        #self.assertEqual("Google",titleofWebpage,"Webpage title is not same, comment should be here") # we both given parameters matches, test case will be passed else fail.

        #assertNotEqual - when expected not equal acutal, test case will be passed.
        self.assertNotEqual("Google",titleofWebpage,"Webpage has same and equal title that y it failed.")

if __name__ == "__main__":
    unittest.main()
