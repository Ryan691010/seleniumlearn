import xlrd, unittest
from ddt import ddt, data, unpack
from selenium import webdriver
import time

def get_data(file_name):
    # create an empty list to store rows
    rows = []
    # open the specified Excel spreadsheet as workbook
    book = xlrd.open_workbook(file_name)
    # get the first sheet
    sheet = book.sheet_by_index(0)
    # iterate through the sheet and get data from rows in list
    for row_idx in range(1, sheet.nrows):
        rows.append(list(sheet.row_values(row_idx, 0, sheet.ncols)))
    return rows


@ddt
class SearchDDT(unittest.TestCase):
    def setUp(self):
        # create a new Firefox session
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

        # navigate to the application home page
        self.driver.get('http://10.20.39.75:8088/bfam6/#/login')

    # specify test data using @data decorator
    @data(*get_data('TestData.xls'))
    @unpack
    def test_search(self, search_value, expected_count):
        #login in
        self.login_name = self.driver.find_element_by_name('username')
        self.login_name.send_keys('zyc')
        self.login_pw = self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div/div[2]/form/div[1]/div[2]/div[2]/div[1]/input')
        self.login_pw.send_keys('zyc111111==')
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div/div[2]/form/div[2]/div/div[2]/button').click()
        # self.login_pw.submit()

        #search 到产品设置界面
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div/div[2]/div[1]/div/ul/div/li[2]').click()
        self.search_field_inner = self.driver.find_element_by_class_name('search')
        self.search_field_inner.send_keys('产品设置')
        self.driver.find_element_by_class_name('menu').click()

        # get the search textbox
        self.search_field = self.driver.find_element_by_xpath('//*[@id="prdSet"]/div[1]/form/div[3]/div/div[1]/input')
        self.search_field.clear()

        # 搜索产品名称
        self.search_field.send_keys(search_value)
        self.driver.find_element_by_xpath('//*[@id="prdSet"]/div[1]/form/div[5]/div[2]/button[1]/span').click()
        time.sleep(3)
        # 得到产品数量信息
        productcount = self.driver\
            .find_element_by_xpath('//*[@id="prdSet"]/div[2]/div[1]/div[1]/div[6]/div/ul/span')

        # check count of products shown in results
        self.assertEqual(expected_count, productcount.text)

    def tearDown(self):
        # close the browser window
        self.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2)