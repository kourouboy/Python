#coding=utf-8
# 鼠标事件
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
bro = webdriver.Firefox()
bro.get("http://news.baidu.com")
qqq = bro.find_element_by_xpath(".//*[@id='s_btn_wr']")
ActionChains(bro).context_click(qqq).perform()
ActionChains(bro).double_click(qqq).perform()
# 定位元素的原位置
element = bro.find_element_by_id("s_btn_wr")
# 定位元素要移动的目标位置
target = bro.find_element_by_class_name("btn")
# 执行元素的移动操作
ActionChains(bro).drag_and_drop(element,target).perform()