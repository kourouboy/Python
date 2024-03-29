__author__ = 'kourouya'
# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re,os

class Testupload(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://localhost:8080/"
        self.verificationErrors = []
        self.accept_next_alert = True
    # 上传文件
    def test_upload(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_name("filename").clear()
        driver.find_element_by_name("filename").send_keys(u"C:\\Users\\13764\\Pictures\\gugu\\gugu2.jpg")
        driver.find_element_by_css_selector("input[type=\"submit\"]").click()
        driver.implicitly_wait(30)
        if driver.find_element_by_partial_link_text(u"gugu2.jpg").is_displayed():
            print "上传成功"
        else:
            print "上传失败"
        driver.quit()
        # 下载文件
    def test_down(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_partial_link_text(u"gugu2.jpg").click()
        driver.implicitly_wait(30)
        if os.path.exists(u"C:\\Users\\13764\\Pictures\\gugu\\gugu2.jpg"):
            print "下载成功"
        else:
            print "下载失败"
        driver.quit()
        # 查看文件
    def test_view(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_xpath(u"(//a[contains(text(),'查看')])[2]").click()
        driver.implicitly_wait(30)
        handles = driver.window_handles
        print(handles)
        driver.switch_to.window(handles[1])
        print(driver.current_window_handle)
        print(driver.title)
        print(driver.current_url)
        driver.quit()
        # 删除上传文件
    def test4_delete(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_xpath("/html/body/div[3]/table/tbody/tr/td[7]/a[2]").click()
        driver.implicitly_wait(30)
        print "删除成功"
        driver.quit()

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)
if __name__ == "__main__":
    unittest.main()