import unittest
from HTMLTestRunner import HTMLTestRunner
import os
from chapter0201 import SearchTest
from cahpter0202 import HomePageTest

# get the directory path to output report file
dir = os.getcwd()
# get all tests from SearchProductTest and HomePageTestclass
search_tests = unittest.TestLoader().loadTestsFromTestCase(SearchTest)
home_page_tests = unittest.TestLoader().loadTestsFromTestCase(HomePageTest)
# create a test suite combining search_test and home_page_test
smoke_tests = unittest.TestSuite([home_page_tests, search_tests])
# open the report file
outfile = open(dir + "\SmokeTestReport.html", "w")
# configure HTMLTestRunner options
runner = HTMLTestRunner.HTMLTestRunner(stream=outfile,title='test_report',description='smoketest')
# run the suite using HTMLTestRunner
runner.run(smoke_tests)