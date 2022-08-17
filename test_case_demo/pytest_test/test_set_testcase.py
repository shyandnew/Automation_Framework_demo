'''
yaml文件设置自动化脚本运行demo
'''
import pytest

from data_demo.yaml_data import OperationYaml
from file_setting_case.Set_case import Setingcase
from base_demo.baes_action import log

data_class = OperationYaml()
data = data_class.get_yaml('../file_setting_case/set_test_case.yaml')

# 断言函数，可以写入日志
def logAssert(Assert, msg):
    if not Assert:
        log.log_out().error(msg)
        assert Assert,msg

class Testsetcase:

    @pytest.mark.set_case
    @pytest.mark.parametrize('case_data', data[1:])
    def test_set_case_(self,case_data):
        print()
        log.log_out().info('---------------{}用例开始--------------'.format(case_data['testcasename']))
        test_case = Setingcase(data[0]['Environment']['url'], data[0]['Environment']['Browser'])
        assert_date = test_case.setcase(case_data['data'])
        logAssert(assert_date==case_data['Expected']['result'], '断言失败!断言详情：%s%s'%(assert_date,"="+case_data['Expected']['result']))
        log.log_out().info('---------------{}用例结束--------------'.format(case_data['testcasename']))
        print()
