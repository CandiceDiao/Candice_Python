# -*- coding: UTF-8 -*-

"""
项目公共内容配置，以及读取配置文件中的配置。这里配置文件用的yaml，也可用其他如XML,INI等，需在file_reader中添加相应的Reader进行处理。
"""
import os

from API_Project.utils.file_reader import YamlReader

import time
import sys

# 所有相关文件的路径

# 通过当前文件的绝对路径，其父级目录一定是框架的base目录，然后确定各层的绝对路径。如果你的结构不同，可自行修改。
# 之前直接拼接的路径，修改了一下，用现在下面这种方法，可以支持linux和windows等不同的平台，也建议大家多用os.path.split()和os.path.join()，不要直接+'\\xxx\\ss'这样
BASE_PATH = os.path.split(os.path.dirname(os.path.abspath(__file__)))[0]
#
# if len(sys.argv) > 1:
#     input = sys.argv[1]
#     if input == 'dev':
#         file = 'config.yml'
#     elif input == 'test':
#         file = 'config_test_env.yml'
# else:
#     file = 'config.yml'

file = 'config.yml'


CONFIG_FILE = os.path.join(BASE_PATH, 'config', file)
# CONFIG_FILE = os.path.join(BASE_PATH, 'config', 'config.yml')
DATA_PATH = os.path.join(BASE_PATH, 'data')
DRIVER_PATH = os.path.join(BASE_PATH, 'drivers')
LOG_PATH = os.path.join(BASE_PATH, 'log')
REPORT_PATH = os.path.join(BASE_PATH, 'report')



class Config:
    def __init__(self, config=CONFIG_FILE):
        # print('配置文件地址：', config)
        self.config = YamlReader(config).data

    def get(self, element, index=0):
        """
        yaml是可以通过'---'分节的。用YamlReader读取返回的是一个list，第一项是默认的节，如果有多个节，可以传入index来获取。
        这样我们其实可以把框架相关的配置放在默认节，其他的关于项目的配置放在其他节中。可以在框架中实现多个项目的测试。
        """
        return self.config[index].get(element)


URL = Config().get('url')  # 从config.yml读取接口地址公共字段
header = Config().get('header')  # 从config.yml读取接口地址公共字段
header_upload = Config().get('header_upload')  # 从config.yml读取接口地址公共字段
Current_Year = time.strftime("%Y", time.localtime())
drg_version = Config().get('drg_version')  # 从config.yml读取接口地址公共字段
icd9_version = Config().get('icd9_version')  # 从config.yml读取接口地址公共字段
icd10_version = Config().get('icd10_version')  # 从config.yml读取接口地址公共字段


if __name__ == '__main__':
    print(file)
    print(type(header))
    print(DATA_PATH)
