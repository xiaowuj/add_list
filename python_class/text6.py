from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def open_url(url,driver):
    driver.get(url)          # 打开一个网站
    driver.maximize_window() #窗口最大化

# def login_page(loginname, nloginpwd, driver):    #登录
#     driver.find_element('id', 'loginname').send_keys('loginname')
#     driver.find_element('id', 'nloginpwd').send_keys('nloginpwd')
#     driver.find_element('id', 'loginsubmit').click()

def search_key(url,driver):
    open_url(url,driver)
    # login_page(loginname, nloginpwd)

    add_input = driver.find_element(By.XPATH, "//input[@type='text']").send_keys("手机")
    add_click = driver.find_element(By.XPATH, "//button[@class='button']").click()
    csdn_text = driver.find_element(By.XPATH, "//div[@id='categorys-2014']//a").text

    if csdn_text == "全部商品分类":
        print("这条用例执行成功 值是:{}".format(csdn_text))
    else:
        print("这条用例执行失败")
