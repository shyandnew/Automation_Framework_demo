'''
 这里实现POM模式的基类，主要封装常用的动作，为页面对象类提供服务。
 这里提前二次封装好常用的selenium常用动作：
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from log.log_demo import Log


log = Log()

class Beas(object):

    def __init__(self, Browser_type=0):
    #启动指定浏览器，如果未指定默认启动谷歌浏览器
        if Browser_type == 'firefox':
            log.log_out().info('打开火狐浏览器')
            self.driver = webdriver.Firefox()
            self.driver.maximize_window()
        elif Browser_type == 'IE':
            log.log_out().info('打开IE浏览器')
            self.driver = webdriver.Ie()
            self.driver.maximize_window()
        else:
            log.log_out().info('打开谷歌浏览器')
            self.driver = webdriver.Chrome('D:\python\chromedriver.exe')
            #self.driver = webdriver.Chrome()
            self.driver.maximize_window()



    # #后期作为流程优化用代码，但是需要创建类时提前创建好driver类
    # def __init__(self,driver):
    #     self.driver = driver


    #基础操作，打开网址
    def get_url(self, url):
        log.log_out().info('打开网址：{}'.format(url))
        self.driver.get(url)

    #基础元素定位
    def locator(self, locator):
        log.log_out().info('定位{}元素'.format(locator))
        return self.driver.find_element(*locator)

    # 获取页面多个元素，返回列表
    def locators(self, locator):
        log.log_out().info('定位{}元素组'.format(locator))
        return self.driver.find_elements(*locator)

    #基础数据输入
    def input_value(self, value, locator):
        log.log_out().info('定位{}元素，输入内容:{}'.format(locator,value))
        self.locator(locator).send_keys(value)

    #基础元素点击
    def click(self, locator):
        log.log_out().info('点击{}元素'.format(locator))
        self.locator(locator).click()

    #基础元素文本获取
    def text(self, locator, label='outerHTML'):
        log.log_out().info('获取{}元素文本'.format(locator))
        text = self.locator(locator).text
        if text == '':
            return self.locator(locator).get_attribute(label)
        else:
            return text

    #基础页面等待动作
    def wait_base(self, time_):
        log.log_out().info('等待{}秒'.format(time_))
        time.sleep(time_)

    # 页面窗口进入
    def Window_switching(self, num):
        log.log_out().info('切换到第{}个窗口的句柄'.format(num))
        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[num])

    # 执行js脚本
    def js_implement(self, js_code):
        log.log_out().info('执行js脚本：{}'.format(js_code))
        self.driver.execute_script(js_code)

    #退出
    def quit(self, closing_mode=0):
        log.log_out().info('退出浏览器')
        if closing_mode == 0:
            self.driver.quit()
        else:
            self.driver.close()

    # 写入内容
    def write_in(self, address, content):
        log.log_out().info('在{}文件中写入{}'.format(address, content))
        with open(address, "a") as e:
            e.write(content)

    # 获取当前时间
    def time_(self, format="%Y-%m-%d"):
        log.log_out().info('获取当前时间：{}')
        return time.strftime(format, time.localtime(time.time()))



if __name__ == '__main__':
    driver = Beas('firefox')
    driver.get_url('http://localhost/phpwind/')
    time.sleep(2)
    abc = (By.CSS_SELECTOR, '[class="btn btn_big btn_submit"]')
    driver.click(abc)
    driver.quit()
