import sys
# sys.path.append(r"C:\Users\zhongyc27701\PycharmProjects\seleniumlearn")
sys.path.append(r"C:\Users\zhongyc27701\PycharmProjects\seleniumlearn\venv\Lib\site-packages")

import unittest
from xmlrunner import xmlrunner
from chapter0201 import SearchTest
from cahpter0202 import HomePageTest

# get all tests from SearchProductTest and HomePageTestclass
search_tests = unittest.TestLoader().loadTestsFromTestCase(SearchTest)
home_page_tests = unittest.TestLoader().loadTestsFromTestCase(HomePageTest)
# create a test suite combining search_test and home_page_test
smoke_tests = unittest.TestSuite([home_page_tests, search_tests])
# run the suite
xmlrunner.XMLTestRunner(verbosity=2, output='test-reports').run(smoke_tests)