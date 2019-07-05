# -*- coding:utf-8 -*-
"Combine tests for gnosis.xml.objectify package (req 2.3+)"
import os,sys,time,unittest
from HTMLTestRunner import HTMLTestRunner

sys.path.append('./src/testcase/login_test')


# 获取文件名为_test.py 的所有用例
#test_dir = './src/testcase/login_test'
test_dir = './src/testcase/vehicle_management'
discover = unittest.defaultTestLoader.discover(test_dir,pattern='*_testA.py')


if __name__ == '__main__':
    nowtime = str(time.strftime("%Y-%m-%d %H_%M_%S"))
    filename = './reports/' + nowtime + '-慧保支撑.html'
    fp = open(filename,'wb')
    runner = HTMLTestRunner(
        stream=fp,
        title=u'慧保支撑V2.1.0',
        description=u'车旺慧保-运营支撑系统测试报告'
    )
    runner.run(discover)
    fp.close()
