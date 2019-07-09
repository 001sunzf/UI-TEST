# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class BusinessManagement(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://192.168.110.85:8095/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_open(self):
		driver = self.driver
		driver.get(base_url + "login.html")
		driver.find_element_by_name("username").clear()
		driver.find_element_by_name("username").send_keys("admin")
		driver.find_element_by_name("pwd").clear()
		drive.find_element_by_xpath('/html/body/div/div[2]/div/form/div/button').click()
		time.sleep(1)
		driver.find_element_by_name("login-btn").click()
		time.sleep(3)
		#切换iframe
		driver.switch_to.frame(0)
		time.sleep(1)
		driver.find_element_by_xpath('//*[@id="add-btn"]').click()
		time.sleep(1)
		#加断言
		self.assertEqual(u'企业名称必填',driver.find_element_id('entName-error').text)
		'''
		self.assertEqual(u'企业类型必填',driver.find_element_by_id('isFormal-error').text)
		self.assertEqual(u'联系人必填',driver.find_element_by_id('linkman-error').text)
		self.assertEqual(u'联系电话必填',driver.find_element_by_id('mobile-error').text)
		self.assertEqual(u'所属行业必填',driver.find_element_by_id('type-error').text)
		self.assertEqual(u'至少省份不为空',driver.find_element_by_id('areaProvince-error').text)
		self.assertEqual(u'所属上级必填',driver.find_element_by_id('parentEntPath-error').text)
		self.assertEqual(u'有效期必填',driver.find_element_by_id('expireDate-error').text)
		'''
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
