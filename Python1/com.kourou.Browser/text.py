#coding=utf-8
from selenium import webdriver
import time
bro = webdriver.Firefox()
bro.get("http://www.baidu.com")
bro.implicitly_wait(30)
# bro.find_element_by_id("kw").send_keys("test")
# bro.find_element_by_id("kw").clear();
# bro.find_element_by_id("kw").send_keys("ztt")
# bro.find_element_by_id("su").submit()
# data = bro.find_element_by_id("cp").text
# print data
# print bro.title
# print bro.current_url
print "浏览器最大化"
bro.maximize_window()
bro.find_element_by_id("kw").send_keys("ztt")
bro.find_element_by_id("su").submit()
time.sleep(2)
bro.quit()
