from selenium import webdriver   #导入webdriver
from python_class import text6   #导入函数文件
from test_data import text_date  #导入测试数据

driver = webdriver.Chrome()   #初始化浏览器
driver.implicitly_wait(10)    #隐式等待
url = text_date.url["url"]    # 取值url地址
#user = text_date["username"]
#pwd = text_date["password"]
text6.search_key(driver=driver,url=url)

