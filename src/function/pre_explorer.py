# -*- coding:utf-8 -*-
from selenium import webdriver
import time,os,re,unittest
from src.common.log import Log
#导入日志模块 Log
log = Log()


def setup(self):
    #初始化登录
    self.driver = webdriver.Firefox()
    self.driver.implicitly_wait(30)
    self.base_url = "http://192.168.110.85:8095/"
    self.verificationErrors = []
    self.accept_next_alert = True


def login_successful(self):
    #登录后关闭企业管理页面
    driver = self.driver
    driver.maximize_window()
    time.sleep(1)
    driver.find_element_by_name('username').clear()
    time.sleep(1)
    driver.find_element_by_name('username').send_keys(u'孙兆富')
    time.sleep(1)
    driver.find_element_by_name('pwd').clear()
    time.sleep(1)
    driver.find_element_by_name('pwd').send_keys('admin123')
    time.sleep(1)
    driver.find_element_by_xpath('/html/body/div/div[2]/div/form/div/button').click()
    print(u'关闭企业管理')


def login_successful_live_business(self):
    #登录后不关闭企业管理
    driver = self.driver
    driver.maximize_window()
    time.sleep(1)
    driver.find_element_by_name('username').clear()
    time.sleep(1)
    driver.find_element_by_name('username').send_keys(u'孙兆富')
    time.sleep(1)
    driver.find_element_by_name('pwd').clear()
    time.sleep(1)
    driver.find_element_by_name('pwd').send_keys('admin123')
    time.sleep(1)
    driver.find_element_by_xpath('/html/body/div/div[2]/div/form/div/button').click()

def current_time(self):
    #格式化系统时间
    current_time = time.strftime('%Y-%m-%d-%H-%M-%S',time.localtime(time.time()))



def in_business_managemet(self):
    driver = self.driver
    driver.get(self.base_url + 'login.html')
    login_successful_live_business(self)
    time.sleep(3)
    #切换iframe
    driver.switch_to.frame(0)
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="add-btn"]').click()
    time.sleep(1)
    #进入下一个iframe
    driver.switch_to.frame('detailFrame')
    #直接电话保存，页面显示必填提示
    driver.find_element_by_id('add-btn').click()
    log.info(u'直接点击保存按钮')