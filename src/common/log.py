# -*- coding:utf-8 -*-
'''
selenium执行时日志类
'''

import logging,time,os
log_path = './logs/'
# 这个是日志存放路径

class Log:
	def __init__(self):
		# 日志文件命名
		self.lognane = os.path.join(log_path,'%s.log'%time.strftime("%Y-%m-%d %H_%M_%S"))
		# 创建logger
		self.logger = logging.getLogger()
		# 设置日志级别
		self.logger.setLevel(logging.DEBUG)
		# 日志输出格式
		self.formatter = logging.Formatter('[%(asctime)s]-%(filename)s[line:%(lineno)d]-fuc:%(funcName)s-%(levelname)s:%(message)s')

	def __console(self,level,message):
		#创建一个fileHandler，用于写日志到本地(fh = logger.FileHandler(self.logger.'w'))
		fh = logging.FileHandler(self.lognane,'a') #追加模式
		fh.setLevel(logging.DEBUG)
		fh.setFormatter(self.formatter)
		#给logger添加handler
		self.logger.addHandler(fh)
		#创建一个StreamHandler，用于输出到控制台
		ch = logging.StreamHandler()
		ch.setLevel(logging.DEBUG)
		ch.setFormatter(self.formatter)
		self.logger.addHandler(ch)

		if level == 'info':
			self.logger.info(message)
		elif level =='debug':
			self.logger.info(message)
		elif level == 'warning':
			self.logger.info(message)
		elif level =='error':
			self.logger.info(message)

		#这两行代码是为了避免日志输出有重复问题
		self.logger.removeHandler(ch)
		self.logger.removeHandler(fh)
		fh.close()

	def debug(self,message):
		self.__console('debug',message)

	def warning(self,message):
		self.__console('warning',message)

	def error(self,message):
		self.__console('error',message)

	def info(self,message):
		self.__console('info',message)


if __name__ == '__main__':
	log = Log()
	log.info(u'--测试开始--')
	log.debug(u'debug日志')
	log.warning(u'警告日志')
	log.error(u'错误日志')