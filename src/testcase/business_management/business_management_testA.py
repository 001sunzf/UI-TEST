# -*- coding:utf-8
from src.function import pre_explorer
from src.function import baseaction
import time,os,sys
import unittest
class BusinessMnagement(unittest.TestCase):
	'''企业管理必填项'''
	def setUp(self):
		pre_explorer.setup(self)

	def test_entName(self):
		'''测试企业名称必填'''
		driver = self.driver
		driver.get(self.base_url + 'login.html')
		pre_explorer.login_successful_live_business(self)
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
		#断言
		self.assertEqual(u'企业名称必填1', driver.find_element_by_id('entName-error').text)
		'''
		self.assertEqual(u'企业类型必填',driver.find_element_by_id('isFormal-error').text)
		self.assertEqual(u'联系人必填',driver.find_element_by_id('linkman-error').text)
		self.assertEqual(u'联系电话必填',driver.find_element_by_id('mobile-error').text)
		self.assertEqual(u'所属行业必填',driver.find_element_by_id('type-error').text)
		self.assertEqual(u'至少省份不为空',driver.find_element_by_id('areaProvince-error').text)
		self.assertEqual(u'所属上级必填',driver.find_element_by_id('parentEntPath-error').text)
		self.assertEqual(u'有效期必填',driver.find_element_by_id('expireDate-error').text)
		'''

	def tearDown(self):
		self.driver.quit()


if __name__ == '__main__':
	unittest.main()


