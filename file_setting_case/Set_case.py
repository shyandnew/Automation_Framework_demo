'''
基础的根据yaml文件设置用例
'''

from data_demo.yaml_data import OperationYaml
from base_demo.baes_action import Beas

# 定义测试用例步骤异常报错
class TestCaseProcedureError(Exception):
    def __init__(self, message):
        self.message = message


class Setingcase:

    def __init__(self, url, Browser=0):
        self.driver = Beas(Browser)
        self.driver.get_url(url)
        self.text = None

    def setcase(self, dict_param):
        for key, value in dict_param.items():
            if 'input' in key:
                self.driver.input_value(value[0], value[1])
                continue
            elif 'click' in key:
                self.driver.click(value)
                continue
            elif 'wait' in key:
                self.driver.wait_base(value)
                continue
            elif 'text' in key:
                if value[1]:
                    self.text = self.driver.text(value[0], value[1])
                else:
                    self.text = self.driver.text(value)
                continue
            elif 'quit' in key:
                if value:
                    self.driver.quit(value[0])
                else:
                    self.driver.quit()
                continue
            elif 'window_to' in key:
                self.driver.Window_switching(value)
                continue
            elif 'write' in key:
                self.driver.write_in(value[0],value[1])
                continue
            elif 'time' in key:
                if value:
                    self.driver.time_(value)
                else:
                    self.driver.time_()
                continue
            elif 'locator' in key:
                self.driver.locator(value)
                continue
            elif 'locators' in key:
                self.driver.locators(value)
                continue
            elif 'js' in key:
                self.driver.js_implement(value)
                continue
            else:
                raise TestCaseProcedureError('用例步骤异常:%s，请检查是否符合规范！'%key)
        if self.text:
            return self.text


if  __name__ == '__main__':
    data = OperationYaml()
    data1= data.get_yaml('set_test_case.yaml')
    brow = data1[0]['Environment']['Browser']
    url = data1[0]['Environment']['url']
    buzhou = data1[1]['data']
    test_case = Setingcase(url,brow)
    text=test_case.setcase(buzhou)
    print(text)