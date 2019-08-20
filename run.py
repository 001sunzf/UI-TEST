# -*- coding:utf-8 -*-
"Combine tests for gnosis.xml.objectify package (req 2.3+)"
import os,sys,time,unittest
from HTMLTestRunner import HTMLTestRunner

sys.path.append('./src/testcase/')


# 获取文件名为_test.py 的所有用例
#test_dir = './src/testcase/login_test'
test_dir = './src/testcase/'
discover = unittest.defaultTestLoader.discover(test_dir,pattern='*_test.py')


if __name__ == '__main__':
    nowtime = str(time.strftime("%Y-%m-%d %H_%M_%S"))
    filename = './reports/' + nowtime + '-慧保支撑.html'
    fp = open(filename,'wb')
    runner = HTMLTestRunner(
        stream=fp,
        title=u'保险风控支撑V2.3.0',
        description=u'主要测试内容企业管理的添加编辑和车辆管理的页面查询功能！'
    )
    runner.run(discover)
    fp.close()
