# -*- coding:utf-8 -*-

from selenium.webdriver.support.ui import WebDriverWait
from src.function import pre_explorer
from src.function.baseaction import BaseAction
import time,unittest
from src.common.log import Log
log = Log()

class VehicleSearh(unittest.TestCase):
    u'''车辆查询'''
    def setUp(self):
        pre_explorer.setup(self)
    def test_search_vehicle_pre(self):
        u'''默认条件查询车辆'''
        dr = self.driver
        dr.get(self.base_url + 'login.html')
        pre_explorer.login_successful(self)
        time.sleep(5)
        log.info(u'-------测试用例开始--------')
        BaseAction(self.driver).find_element('xpath','/html/body/div/div[2]/div[3]/div[1]/div[1]/div/a[2]')
        log.info(u'测试结束')

    def tearDown(self):
        self.driver.quit()
        log.info(u'关闭浏览器，测试用例退出')

if __name__ == "__main__":
    unittest.main()


