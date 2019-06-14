# -*- coding:utf-8 -*-

from selenium import webdriver
import os,re,time

class BaseAction(object):
	"""对元素操作的方法禁行封装"""

	def __init__(self, driver):
		self.driver = driver

	def find_element(self,ele_type,value):
		'''查询页面元素，增加显性等待时间
		Args:
			ele_type(str):元素定位方式
			value(str):元素定位属性值
		Returns:
			ele(WebElement):返回查找对象
		'''

		ele = None
		try:
			if ele_type == 'id':
				WebDriverWait(self.driver,15).until(lambda driver: driver.find_element_by_id(value))
				ele = self.driver.find_element_by_id(value)
			elif ele_type == 'name':
				WebDriverWait(self.driver,15).until(lambda driver: driver.find_element_by_name(value))
				ele = self.driver.find_element_by_name(value)
			elif ele_type =='link_text':
				WebDriverWait(self.driver,15).until(lambda driver: driver.find_element_by_link_text(value))
				ele = self.driver.find_element_by_link_text(value)
			elif ele_type == 'partial_link_text':
				WebDriverWait(self.driver,15).until(lambda driver: driver.find_element_by_partial_link_text(value))
				ele = self.driver.find_element_by_partial_link_text(value)
			elif ele_type == 'tag_name':
				WebDriverWait(self.driver,15).until(lambda driver: driver.find_element_by_tag_name(value))
				ele = self.driver.find_element_by_tag_name(value)
			elif ele_type == 'xpath':
				WebDriverWait(self.driver,15).until(lambda driver: driver.find_element_by_xpath(value))
				ele = self.driver.find_element_by_xpath(value)
			else:
				print('没有这种元素定位方式{}'.format(ele_type))
		except NoSuchElementException,e:
			print(e.msg)
		except TimeoutException,e:
			print(e.msg)
		else:
			return ele

	def set_value_by_h5(self,html_dic,value_dic):
		'''给页面元素批量赋值
		agrs：html_dic(dict):webview元素控件定位组成字典
				value_dic(dict):输入的值组成的字典
		'''
		for key in html_dic:
			if key in value_dic:
				html_list = html_dic[key].split('|')
				html_type = html_list[1]
				html_value = html_list[0]
				ele = self.find_element(html_type,html_value)
				self.sendkeys_by_h5(ele,value_dic[key])
			else:
				self.logger.error('要输入的值字典中没有这个{}字段').format(key)
				print('要输入的值字典中没有这个{}字段'.format(key))

	def sendkeys_by_h5(self,ele,value):
		'''
		给Webview页面根据控件元素标签类型输入值
		agrs：
			ele(WebElement):页面控件元素对象
			value（str):页面控件元素要输入的值
		'''
		tag_name = ele.tag_name
		if tag_name == 'input':
			input_type = ele.get_attribute('type')
			if input_type == 'text' or 'password':
				self._send_keys(ele,value)
			elif input_type == 'radio':
				self._select_radio(ele)
			elif input_type == 'checkbox':
				self._select_checkbox(ele)
			elif tag_name == 'select':
				self._select_select(ele,value)
			elif tag_name == 'textarea':
				self._send_keys(ele,value)
			elif tag_name == 'file':
				# 图片路径分隔符处理
				value = value.replace('/',os.path.sep)
				value = value.replace('\\',os.path.sep)
				# 相对路径处理
				if not os.path.exists(value):
					value = image_dir + value
				value = os.path.realpath(value)
				ele.send_keys(value)

	def _select_radio(self,ele):
		'''点击webveiw页面元素中的单选按钮
		args:
			ele（WebElement)：单选按钮控件元素对象
		'''
		r = ele.is_selected()
		if not r:
			ele.click()

	def _select_checkbox(self,ele):
		'''选择webview页面元素中的多选按钮
		Args：
			ele(WebElement):多选按钮控件元素中的单一选择对象
		'''
		r = ele.is_selected()
		if not r:
			ele.click()

	def _select_select(self,ele,value):
		'''选择webview页面元素的选择框
		Args:
		ele(webelement):多选控件元素对象
		value(str):选择文本框
		'''
		s = Select(ele)
		s.select_by_visible_text(value)
		


		
