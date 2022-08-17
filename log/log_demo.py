'''
日志模块类实现
'''

import logging
import time
import os
from data_demo.yaml_data import OperationYaml


class Log:

    def __init__(self, filename=0):
        # 读取配置文件信息
        Log_conf = OperationYaml()
        data = Log_conf.get_yaml('../log/log_configuration.yaml')
        self.log_format = data['log_format']
        self.log_level = data['log_level']
        self.log_filename_format = data['log_filename_format']
        self.log_del_threshold = data['log_del_threshold']
        self.Console_out = data['Console_out']
        self.filename = filename
        time_ = time.strftime(self.log_filename_format, time.localtime(time.time()))
        self.log_file_name = '../log/logs/' + str(time_) + '_demo_logs.log'
        # 每次创建对象，检查日志，清除老旧日志
        self.log_del(self.log_del_threshold[0], self.log_del_threshold[1])
        #控制台输出日志准备
        if self.Console_out != 0:
            # 控制台输入日志代码

            # 实例化日志类
            self.loger = logging.getLogger()
            # 设置日志级别
            self.loger.setLevel(self.log_level)
            # 创建一个控制台
            Console = logging.StreamHandler()
            # 创建一个格式器
            format = logging.Formatter(fmt=self.log_format)
            # 把格式添加给控制器
            Console.setFormatter(format)
            # 控制台添加到日志类中
            self.loger.addHandler(Console)

            # 文件中写入日志

            # 创建一个日志文件，并添加到实例化的日志类中
            if filename == 0:
                file = logging.FileHandler(self.log_file_name, encoding='utf-8')
            else:
                file = logging.FileHandler(filename, encoding='utf-8')
            self.loger.addHandler(file)
            # 设置文件日志格式
            file.setFormatter(format)

    # 日志清理
    def log_del(self, threshold, del_num):
        log_num = os.listdir('../log/logs')
        if len(log_num) >= threshold:
            for i in range(0, del_num):
                os.remove('../log/logs/' + log_num[i])

    def log_out(self):
        if self.Console_out != 0:
        #if self.loger:
            return self.loger
        else:
            if self.filename == 0:
                logging.basicConfig(level=self.log_level, format=self.log_format, filename=self.log_file_name)
                return logging
            else:
                logging.basicConfig(level=self.log_level, format=self.log_format, filename=self.filename)
                return logging


if __name__ == '__main__':
    a=Log()
    a.log_out().info('这是一个测试')
