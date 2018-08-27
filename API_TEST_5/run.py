__author__ = 'zz'
import os
import time
import unittest
import HTMLTestRunnerNew
from conf import read_path
from public.test_http_request import TestHttpRequest
from public.send_email import sendEmail


suite=unittest.TestSuite()#suite 测试套件  负责收集用例

loader=unittest.TestLoader()
suite.addTest(loader.loadTestsFromTestCase(TestHttpRequest))

now=time.strftime('%Y-%m-%d_%H_%M_%S')
path=os.path.join(read_path.report_path,'test_api'+now+'.html')
with open(path,"wb+") as file:
    runner=HTMLTestRunnerNew.HTMLTestRunner(stream=file,title='0727_api_test',description='6666',tester='华华')
    runner.run(suite)

#发送邮件
#sendEmail().send_email('204893985@qq.com',path)
