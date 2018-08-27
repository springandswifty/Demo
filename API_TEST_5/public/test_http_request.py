__author__ = 'zz'
import unittest

from ddt import ddt,data

from public.read_config import ReadConfig
from public.http_requests import HttpRequest
from public.do_excel import DoExcel
from public.my_log import MyLog
from conf import read_path

#测试数据
ip=ReadConfig().read_config(read_path.config_path,'IP','ip')
mode=ReadConfig().read_config(read_path.config_path,'FLAG','mode')
case_id_list=ReadConfig().read_config(read_path.config_path,'FLAG','case_id_list')
test_data=DoExcel(read_path.test_data_path,'test_data',mode,case_id_list).do_excel()

#创建一个日志对象
logger=MyLog('python8')

#全局变量 COOKIES
COOKIES=None

@ddt
class TestHttpRequest(unittest.TestCase):
    def setUp(self):#执行用例之前的准备工作
        logger.info("我要开始测试啦！")
        self.t=DoExcel(read_path.test_data_path,'test_data',mode,case_id_list)
        #保存测试结果的实例

    @data(*test_data)#拆分数据
    def test_api(self,item):#测试类里面的函数没有传参
        global COOKIES#声明全局变量
        #执行http请求
        res=HttpRequest().http_request(ip+item['url'],eval(item['param']),item['method'],COOKIES)

        #每次请求之后就判断 是否产生COOKIES  如果产生 就替换全局变量
        #如果不产生 就不替换
        if res.cookies!={}:#就说该请求应该是登录请求 产生了cookie 类字典
            COOKIES=res.cookies

        #保存测试结果
        self.t.write_data(item['case_id']+1,7,str(res.json()))
        try:
            self.assertEqual(eval(item['ExpectedResult']),res.json())#断言的作用？对比期望值与实际值
            test_result='PASS'
        except AssertionError as e:
            logger.error("执行用例的时候报错:{0}".format(e))
            test_result='FAIL'
            raise e#处理完异常之后  记得丢出去~异常不要留在家里
        finally:#不管怎样 都要写入结果值
            self.t.write_data(item['case_id']+1,8,test_result)#保存测试对比结果

    def tearDown(self):
        logger.info("我已经结束测试啦！")

