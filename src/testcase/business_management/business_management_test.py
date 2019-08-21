# -*- coding:utf-8
from src.function import pre_explorer
from src.function import baseaction
import time,os,sys
import unittest
from src.common.log import Log
log = Log()
class BusinessMnagement(unittest.TestCase):
	'''企业管理必填项'''
	def setUp(self):
		pre_explorer.setup(self)

	def test_entName(self):
		'''测试企业名称必填'''
		driver = self.driver
		pre_explorer.in_business_managemet(self)
		#断言
		self.assertEqual(u'企业名称必填1', driver.find_element_by_id('entName-error').text)
		log.info(u'测试企业名称必填通过')

	def test_isForm_error(self):
		'''测试企业类型必填'''
		driver = self.driver
		pre_explorer.in_business_managemet(self)
		#断言
		self.assertEqual(u'企业类型必填',driver.find_element_by_id('isFormal-error').text)
		log.info(u'测试企业类型必填通过')

	def test_linkman_error(self):
		'''测试联系人必填'''
		driver = self.driver
		pre_explorer.in_business_managemet(self)
		#断言
		self.assertEqual(u'联系人必填',driver.find_element_by_id('linkman-error').text)
		log.info(u'测试联系人必填通过')

	def test_mobile_error(self):
		'''测试联系电话必填'''
		driver = self.driver
		pre_explorer.in_business_managemet(self)
		#断言
		self.assertEqual(u'联系电话必填',driver.find_element_by_id('mobile-error').text)
		log.info(u'测试联系电话必填')

	def test_type_error(self):
		'''测试所属行业必填'''
		driver = self.driver
		pre_explorer.in_business_managemet(self)
		#断言
		self.assertEqual(u'所属行业必填',driver.find_element_by_id('type-error').text)
		log.info(u'测试所属行业必填')

	def test_areaProvince_error(self):
		'''测试省份必选'''
		driver = self.driver
		pre_explorer.in_business_managemet(self)
		#断言
		self.assertEqual(u'至少省份不为空',driver.find_element_by_id('areaProvince-error').text)
		log.info(u'测试省份必填通过')

	def test_parentEntPath_error(self):
		'''测试所属上级必填'''
		driver = self.driver
		pre_explorer.in_business_managemet(self)
		#断言
		self.assertEqual(u'所属上级必填',driver.find_element_by_id('parentEntPath-error').text)
		log.info(u'测试所属上级必填通过')

	def test_expireDate_error(self):
		'''测试有效期必填'''
		driver = self.driver
		pre_explorer.in_business_managemet(self)
		#断言
		self.assertEqual(u'有效期必填',driver.find_element_by_id('expireDate-error').text)
		log.info(u'测试有效期必填通过')


	def tearDown(self):
		self.driver.quit()


if __name__ == '__main__':
	unittest.main()


