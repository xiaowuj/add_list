# list1 = ("1", 2, 3)
# list2 =list(list1)
# list2[0] = 1
# print(list2)


# for j in range(10):
#     print(j)
# sum = 0
# for i in range(num):  # 依次循环获取每个数
#     sum = sum + int(j[:i + 1])  # 将字符串转换成数，然后进行求和
# print(sum)

# for i in range(10):
#     print(i)
#
# list1 = [5, 4, 56, 6432, 234, 777, 432, 4]
# for name in list1:
#
#    if list1 > list1.len(5):
#     print("dad")

from selenium import webdriver
from selenium.webdriver.common.by import By

# 打开百度

driver = webdriver.Chrome()  # 选择浏览器
driver.get("https://www.jd.com/?cu=true&utm_source=baidu-pinzhuan&utm_medium=cpc&utm_campaign=t_288551095_baidupinzhuan&utm_term=0f3d30c8dba7459bb52f2eb5eba8ac7d_0_7ad9abd17a87404fb9203a2ec59b1a37")  # 打开一个网站
driver.implicitly_wait(10)
# driver.get("https://www.taobao.com/")
# driver.maximize_window()                 #窗口最大化
# time.sleep(2)                            #等待默认2秒
# driver.get("https://www.mi.com/")
# driver.back()                            #后退上一个页面
# driver.forward()                         #前进下一个页面
# driver.refresh()                         #刷新页面
# driver.close("https://www.baidu.com/")   #关闭tab页 关闭当前窗口
# driver.quit()                             #关闭浏览器
#driver.find_element(By.XPATH, "//div[@class='item item-fore1']/input").send_keys('小吴')
# driver.find_element('name','loginname').send_keys('小吴')
# driver.find_element('id','nloginpwd').send_keys('小吴')
# driver.find_element('id','loginsubmit').click()
"""
xpath:
1、绝对路径: /HTML/body,div/div/div ——跟节点,顺序性,继承关键  工作里不能用
2、相对路径: 只靠自己的特征定位
   标签名+属性+//标签名[@id属性名="属性值"]
"""

# driver.find_element(By.XPATH, "//input[@class='itxt']").send_keys("小吴")
# driver.find_element(By.XPATH, '//input[@id="nloginpwd"]').send_keys("小吴")

#文本属性定位
# adsa=driver.find_element(By.XPATH, "//p[text()='《网络安全法》']").text
# adsa=driver.find_element(By.XPATH, "//p[contains(text(),'依据')]/a").text  包含属性文本定位
# print(adsa)
# add = driver.find_element(By.XPATH, "//div[@class='item item-fore5']//a").text
# #class定位
# if add == "登    录":
#     print("这条用例了测试通过")
# else:
#     print("这条用例测试失败")


"""
文本定位
"""

# add = driver.find_element(By.XPATH, "//li[@data-index='0']").text
# add = driver.find_element(By.XPATH, "//li[@clstag='h|keycount|head|navi_01']/a").click()

add_input = driver.find_element(By.XPATH, "//input[@type='text']").send_keys("手机")
add_click = driver.find_element(By.XPATH, "//button[@class='button']").click()
csdn_text = driver.find_element(By.XPATH, "//div[@id='categorys-2014']//a").text #获取属性值
# add_clickdsad = driver.find_element(By.XPATH, "//div[@class='form']")
# # csd = driver.find_element(By.XPATH, "//li[@clstag='h|keycount|h|keycount|head|category_01a']/a").click()
# #add = driver.find_element(By.XPATH, "//a[text()='电脑']").text #获取文本值
if csdn_text == "全部商品分类":
    print("这条用例执行成功 值是:{}".format(csdn_text))
else:
    print("这条用例执行失败")











