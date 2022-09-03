# This is demo for unittest - setup method and teardown method

import unittest




class AppTesting(unittest.TestCase):

    # intialize webdriver here


    @unittest.SkipTest # these are decorators
    def test_search(self): # test_method 1
        print("This is search test")


    @unittest.skip("I am skipping this test method it is not yet ready")     # skip test with a reason
    def test_advancedSearch(self): # test_method 2
        print("This is advanced search test")

    @unittest.skipIf(1==1 , " 1 is equal to 1, we need to pass some comments here") # skip test based on a condition
    def test_prepaidRecharge(self): # test_method 3
        print("this is prepaid REcharge test")

    def test_postpaidRecharge(self): # test_method 4
        print("This is postpaid recharge test")

    def test_loingByGmail(self):
        print("this is login by gmail")

    def test_loginbyTwitter(self):
        print("this is login by twitter")




if __name__ == "__main__":
    unittest.main() # this will run all test method above.
