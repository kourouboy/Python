
#coding=utf-8
from selenium import webdriver
import time
# 浏览器的前进 后退 
bro = webdriver.Firefox()
# 访问百度首页
first_url = 'http://www.baidu.com'
print "now access %s" %(first_url)
bro.get(first_url)
time.sleep(2)
# 访问新闻页面
second_url = 'http://news.baidu.com'
print "now access %s" %(second_url)
bro.get(second_url)
time.sleep(2)
# 返回（后退）到百度首页
print "back to %s" %(first_url)
bro.back()
time.sleep(2)
# 前进到新闻页面
print "forward to %s" %(second_url)
bro.forward()
time.sleep(2)
bro.quit()
