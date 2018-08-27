# * coding:utf-8 *
# author : '阿虾'


# 完成register、登录接口的请求：
# 1：请自己把测试数据写到Excel里面去（具体参数 url请参考测试文档，测试接口地址我会发课堂派）
# （每个接口要有2条用例，一正常一个异常）
# 2：编写一个Excel读取和存储测试数据的类，从1中获取必要的测试数据，
# 每一行数据存在一个字典里面，所有行数据存在一个大列表列表。
# 3：编写一个HTTP请求类能够完成register接口、login接口的测试
# 4：创建实例利用第二步里面的Excel操作类读取到的数据完成接口的测试，并同步把测试结果存到Excel中。
# 接口地址：http://119.23.241.154:8080/futureloan/mvc/api/member/register
# 请大家根据各自的端口做好端口的切换
import requests

from public.my_log import MyLog


logger=MyLog('python10')

class HttpRequest:
    def http_request(self,url,param,method,cookies):
        if method.lower() == 'get':
            try:
                res = requests.get(url,param,cookies=cookies)
            except Exception as e:
                logger.error('请求出错:{0}'.format(e))

        elif method.lower() == 'post':
             try:
                res = requests.post(url,param,cookies=cookies)
             except Exception as e:
                logger.error('请求出错:{0}'.format(e))
        else:
            logger.error('请求错误！')
        return res


