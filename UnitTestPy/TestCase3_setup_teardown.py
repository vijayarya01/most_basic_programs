# This is demo for unittest - setup method and teardown method

import unittest


def setUpModule():
    print("setUpModule")


def tearDownModule():
    print("tearDownModule")


class AppTesting(unittest.TestCase):

    # intialize webdriver here

    @classmethod # these are decorators
    def setUp(self): # this setup method will execute each time before execution of test_methods
        print("this is login test")

    @classmethod # these are decorators
    def tearDown(self):  # this setup method will execute each time after execution of test_methods
        print("this is logout  test")

    @classmethod # will run just once before all test methods # these are decorators
    def setUpClass(cls):
        print("Open Application")

    @classmethod # will run just once after all test methods
    def tearDownClass(cls):
        print("Close application")


    def test_search(self): # test_method 1
        print("This is search test")
    def test_advancedSearch(self): # test_method 2
        print("This is advanced search test")

    def test_prepaidRecharge(self): # test_method 3
        print("this is prepaid REcharge test")

    def test_postpaidRecharge(self): # test_method 4
        print("This is postpaid recharge test")

if __name__ == "__main__":
    unittest.main() # this will run all test method above.
