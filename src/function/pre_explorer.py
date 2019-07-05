# -*- coding:utf-8 -*-
from selenium import webdriver
import time,os,re,unittest
from src.common.log import Log
log = Log()


def setup(self):
    self.driver = webdriver.Firefox()
    self.driver.implicitly_wait(30)
    self.base_url = "http://192.168.110.85:8095/"
    self.verificationErrors = []
    self.accept_next_alert = True


def login_successful(self):
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

def current_time(self):
    current_time = time.strftime('%Y-%m-%d-%H-%M-%S',time.localtime(time.time()))

