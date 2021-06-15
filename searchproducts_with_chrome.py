import os
from selenium import webdriver

# get the path of chromedriver
dir = os.path.dirname(__file__)
chrome_driver_path = dir + "\chromedriver.exe"
#remove the .exe extension on linux or mac platform

# create a new Chrome session
driver = webdriver.Chrome(chrome_driver_path)
driver.implicitly_wait(30)
driver.maximize_window()

# navigate to the application home page
driver.get('http://www.baidu.com')

# get the search textbox
search_field = driver.find_element_by_id("kw")

#get the value of maxlength attributer
att01 = search_field.get_attribute("maxlength")
print(att01)
#获取元素内的全部HTML
att02 = search_field.get_attribute("outerHTML")
print(att02)

#清空输入
search_field.clear()
# enter search keyword and submit
search_field.send_keys('phones')
search_field.submit()

# get all the anchor elements which have product names displayed
# currently on result page using find_elements_by_xpath method
products = driver.find_elements_by_xpath('//a[contains(text(),"HUAWEI")]')
# get the number of anchor elements found
print ("Found " + str(len(products)) + " products:")
# iterate through each anchor element and
# print the text that is name of the product
for product in products:
    print (product.text)
    #print (product.get_attribute('innerHTML'))
    #print (product.get_attribute('outerHTML'))

#get button elements
# buttons = driver.find_elements_by_class_name("op_dict_text2")
# print (str(len(buttons)))
# for button in buttons:
#     print(button.get_attribute('textContent'))

#get all pics
pics = driver.find_elements_by_tag_name("img")
print("found "+str(len(pics))+" pics")

#找到文本为百度百科的元素
linkbaike = driver.find_element_by_partial_link_text("进行")
print(linkbaike.get_attribute('outerHTML'))

# close the browser window
driver.quit()