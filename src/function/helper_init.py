# -*- coding:utf-8 -*-

'''读取init配置文件工具类'''

import os,sys,re
import time,configparser
#configparser 模块主要使用模块中RawConfigParser()，ConfigParser()、SafeConfigParse()这三个方法（三选一），创建一个对象使用对象的方法对配置文件进行增删改查操作

#解决ConfigParser option无论大小写，都会转换车小写的问题

#def optionxform(self,optionstr):

#RawConfigParser().optionxform = optionxform

#解决UnicodeDecodeError
#reload(sys)
#sys.setdefaultencoding('utf-8')

class IniHelper(object):
    '''
    读取ini配置文件工具类

    def __init__(self,file_name,path=''):
        ''处理file_name为绝对路径
        Args:
            file_name(str):配置文件名称
        ''
        data_path = path
        file_name = unicode(file_name)
        if os.path.exists(file_name):
            self.file_name = file_name
        else:
            self.file_name = ''.join([unicode(data_path),file_name])
            self.read_handle = None
            self.cfg = self.ini_read()
'''
    def _get_read_handle(self):
        '''为解决编码问题，用codecs内置模块打开文件，处理编码utf-8编码或utf-8-sig编码的文件'''
        cfg = configparser.ConfigParer()
        try:
            with codecs.open(self.file_name,'r','utf-8-sig') as handle:
                cfg.readfp(handle)
                return cfg
        except UnicodeDecodeError:
            with codecs.open(self.file_name,'r') as handle:
                cfg.readfp(handle)
                return cfg
        except IOError as e:
            print(u'找不到这个文件{0}').format(self,file_name)
            print(e.message)

    def get_value(self,section,option):
        '''获取ini配置文件中section组下的option的值
        Args:
            section(str):section name
            option(str):option name
        Returns:
            value(str):section 下的option的值
        '''
        try:
            value = self.cfg.get(unicode(section),unicode(option))
        except NpSectionError as e:
            print(''.join([u'没有找到section名称',section,e.message]))
        except NoOptionError as e:
            print(''.join([u'没有找到option名称',option,e.message]))
        else:
            return value

