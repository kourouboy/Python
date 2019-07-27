
#coding=utf-8
from selenium import webdriver
import time
# 控制浏览器滚动条
bro = webdriver.Firefox()
bro.get("http://baidu.com")
# 搜索
bro.find_element_by_id("kw").send_keys("selenium")
bro.find_element_by_id("su").submit()
time.sleep(2)
# 将页面滚动条拖到底部
js = "var q=document.documentElement.scrollTop=10000"
bro.execute_script(js)
time.sleep(2)
# 将滚动条拖到页面的顶部
js="var q=document.documentElement.scrollTop=0"
bro.execute_script(js)
time.sleep(3)
bro.quit()