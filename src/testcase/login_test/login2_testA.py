# -*- coding:utf-8 -*-

from selenium import webdriver
import unittest, time
from src.function.login import LoginPage
from src.function.baseaction import BaseAction as f
from src.function.helper_init import IniHelper
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
        # 用户名和密码正确，登录成功
        log.info(u'--用户名和密码正确测试用例开始--')
        ele_dic = IniHelper(u'元素标识.ini',u'用户和密码').get_section_dic(u'账号')
        log.info(u'测试通过')



    def tearDown(self):
        self.driver.quit()
        log.info(u'--测试结束--')


if __name__ == "__main__":
    unittest.main()