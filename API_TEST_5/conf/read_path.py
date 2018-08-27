__author__ = 'zz'
import os
from public.read_config import ReadConfig

config_path=os.path.join(os.path.split(os.path.realpath(__file__))[0],'auto.conf')

#顶级目录读取出来  项目的路径
project_path=ReadConfig().read_config(config_path,'PROJECT_PATH','project_path')

#测试数据的存储的路径
test_data_path=os.path.join(project_path,'test_data','test_api_1.xlsx')

#测试日志的存储路径
log_path=os.path.join(project_path,'test_result','test_log')

#测试报告的存储路径
report_path=os.path.join(project_path,'test_result','html_report')
