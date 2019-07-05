# -*- coding = utf-8 -*-

import configparser
#这个类继承configparser,解决option大写被转换成小写的问题
class MyConfiParer(configparser.ConfigParser):
    def __init__(self,defaults=None):
        configparser.ConfigParser.__init__(self,defaults=defaults)

    def options(self, optionstr):
        return optionstr