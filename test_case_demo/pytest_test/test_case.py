'''
常规测试用例编写
'''

import pytest
from page_demo.page_action import *
from data_demo.data_value import *

class Testcase:

    @pytest.mark.smoke
    @pytest.mark.parametrize('case_data', [['shy', '123456']])
    def test_01(self, case_data):
        log.log_out().info('----------用例开始----------')
        login = Login_page()
        text = login.login_action(case_data[0], case_data[1])
        assert text == 'shy'
        log.log_out().info('----------用例结束----------')

    @pytest.mark.smoke
    @pytest.mark.parametrize('case_data', Data_demo().data_input('username', 'password'))
    def test_02(self, case_data):
        log.log_out().info('----------用例开始----------')
        login = Login_page()
        text = login.login_action(case_data[0], case_data[1])
        assert text == None or '登录失败！' in text
        log.log_out().info('----------用例结束----------')


