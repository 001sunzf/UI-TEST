# -*- coding:utf-8 -*-
"Combine tests for gnosis.xml.objectify package (req 2.3+)"
import os,sys,time,unittest
from HTMLTestRunner import HTMLTestRunner

sys.path.append('./src/testcase/login_test')

# 获取文件名为_test.py 的所有用例
test_dir = './src/testcase/login_test'
discover = unittest.defaultTestLoader.discover(test_dir,pattern='*_test.py')

if __name__ == '__main__':
    nowtime = str(time.strftime("%Y-%m-%d %H_%M_%S"))
    filename = './reports/' + nowtime + '-慧保支撑.html'
    fp = open(filename,'wb')
    runner = HTMLTestRunner(
        stream=fp,
        title=u'慧保支撑V1.4.6',
        description=u'慧保支撑登录和系统管理测试报告'
    )
    runner.run(discover)
    fp.close()
