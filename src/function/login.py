# -*- coding:utf-8 -*-

import selenium,time
class LoginPage(object):
    '''登录页面'''

    def __init__(self,driver):
        self.driver = driver

    def username_ele(self):
        '''返回用户名输入框'''
        ele = self.driver.find_element_by_name('username')
        return ele

    def pwd_ele(self):
        '''返回密码输入框'''
        ele = self.driver.find_element_by_name('pwd')
        return ele

    def remember_load_ele(self):
        '''记住登录信息按钮'''
        ele = self.driver.find_element_by_class_name('custom-checkbox')
        return ele
    def login_btn_ele(self):
        '''点击登录按钮'''
        ele = self.driver.find_element_by_xpath('/html/body/div/div[2]/div/form/div/button')
        return ele

    def login_by_username_pwd(self,username,pwd):
        '''登录业务'''
        username_ele = self.username_ele()
        username_ele.send_keys(username)
        time.sleep(2)
        pwd_ele = self.pwd_ele()
        pwd_ele.send_keys(pwd)
        time.sleep(2)
        login_btn = self.login_btn_ele()
        login_btn.click()
        time.sleep(2)

    def jsa(self):   
        #self.js1 = "document.getElementsByClassName($'hidden'[0]).removeClass('hidden')"
        #js1 = 'document.getElementsByClassName($"hidden")[0].removeClass("hidden")';
        #js1 = 'setTimeout(function(){window.page.pageVm.isShowError = false},1000)';
        js1 = 'window.page.pageVm.isShowError = true'
        
        self.driver.execute_script(js1)






