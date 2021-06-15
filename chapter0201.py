import unittest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
# from __builtin__ import classmethod

class SearchTest (unittest.TestCase):
    @classmethod
    def setUp(cls):
        #创建一个火狐浏览器实例
        cls.driver=webdriver.Firefox()
        cls.driver.implicitly_wait(5)
        # cls.driver.maximize_window()

        #navigate to the application home page
        cls.driver.get('http://www.baidu.com')

    def test_search_by_category(self):
        # get the search textbox
        self.search_field = self.driver.find_element_by_name("wd")
        self.search_field.clear()

        # enter search keyword and submit
        self.search_field.send_keys("phones")
        self.search_field.submit()
        # get all the anchor elements which have product names
        # displayed currently on result page using
        # find_elements_by_xpath method
        products = self.driver.find_elements_by_xpath('//a[contains(text(),"HUAWEI")]')
        self.assertEqual(1, len(products),"这个有啥用，就是不相等呗")

    @classmethod
    def tearDown(cls):
        # close the browser window
        cls.driver.quit()


    def test_search_by_name(self):
        # get the search textbox
        self.search_field = self.driver.find_element_by_name("wd")
        self.search_field.clear()
        # enter search keyword and submit
        self.search_field.send_keys("salt shaker")
        self.search_field.submit()
        # get all the anchor elements which have
        # product names displayed
        # currently on result page using
        # find_elements_by_xpath method
        products = self.driver.find_elements_by_xpath('//div/span[@class="head-singer_ibQWz"]')
        self.assertEqual(1, len(products))


if __name__ == '__main__':
    unittest.main(verbosity=2)