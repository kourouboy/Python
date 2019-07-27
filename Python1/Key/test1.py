#coding=utf-8
# 键盘按键用法
from selenium import webdriver
# 引入Keys包
from selenium.webdriver.common.keys import Keys
import os,time
bro = webdriver.Firefox()
bro.get("http://demo.zentao.net/user-login-Lw==.html")
time.sleep(2)
bro.find_element_by_id("account").clear()
time.sleep(2)
bro.find_element_by_id("account").send_keys("demo")
time.sleep(2)
# tab的定位相当于清除了密码框的默认提示信息，等同上面的clear（）
bro.find_element_by_id("account").send_keys(Keys.TAB)
time.sleep(2)

# 通过定位密码框，enter来代替登陆按钮
bro.find_element_by_name("password").send_keys(Keys.ENTER)
time.sleep(2)
bro.quit()
