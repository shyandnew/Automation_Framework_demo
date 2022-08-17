'''
pytest总体运行文件
'''
import os
import sys
curPath = os.path.abspath(os.path.dirname('..\data_demo\yaml_data.py'))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
import pytest
from data_demo.yaml_data import OperationYaml



def run():
    run_data = OperationYaml().get_yaml('run_to_configure.yaml')
    pytest.main(run_data['pytest'])
    if run_data['os'] != None:
        os.system(run_data['os'])
    else:
        return

if __name__ == '__main__':
    run()
