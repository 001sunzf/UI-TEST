# -*- coding:utf-8 -*-

from selenium import webdriver
import unittest, time
from src.function.login import LoginPage
from src.common.log import Log
log = Log()
class LoginTest(unittest.TestCase):
    '''登录测试用例'''

    def setUp(self):
        '''初始化测试用例'''
        self.driver = webdriver.Firefox()
        self.driver.get('http://192.168.110.85:8095/login.html')
        time.sleep(1)

    
    def test_login_01(self):
        #用户名和密码正确，登录成功
        log.info(u'--用户名和密码正确测试用例开始--')
        LoginPage(self.driver).login_by_username_pwd(u'孙兆富','admin123')
        log.info(u'寻找断点')
        self.assertEqual(u'孙兆富',self.driver.find_element_by_xpath('/html/body/div/div[1]/div/div[1]/span[2]').text)
        log.info(u'测试通过')
    '''

    def test_login_02(self):
        #用户名和密码错误，登录失败
        log.info(u'--用户名正确密码错误测试用例开始--')
        LoginPage(self.driver).login_by_username_pwd(u'孙兆富','admin1234')
        log.info(u'寻找断点')
      
        self.js2 = self.driver.find_element_by_css_selector("div.tip-message").text

        self.assertEqual(u'用户或密码错误',self.js2)
        log.info(u'测试通过')
    '''
        

    def tearDown(self):
        self.driver.quit()
        log.info(u'--测试结束--')

if __name__ == "__main__":
    unittest.main()