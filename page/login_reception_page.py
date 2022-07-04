from selenium.webdriver.common.by import By
from common.bases import Bases
from common.logger import Logger


class LoginReceptionPage(object):

    def __init__(self):
        self.bs = Bases()
        self.log = Logger()

    # 手机号/邮箱
    def get_login_username(self):
        try:
            res = self.bs.find_id('username')
            # res = self.bs.driver.find_element(by=By.ID,value='username')
        except Exception:
            self.log.getLog(element='查找"手机号/邮箱"失败')
            raise
        return res

    # 密码
    def get_login_password(self):
        try:
            res = self.bs.find_id('password')
            # res = self.bs.driver.find_element(by=By.ID,value='password')
        except Exception:
            self.log.getLog(element='查找"密码"失败')
            raise
        return res

    # 验证码
    def get_login_code(self):
        try:
            res = self.bs.find_id('verify_code')
            # res = self.bs.driver.find_element(by=By.ID,value='verify_code')
        except Exception:
            self.log.getLog(element='查找"验证码"失败')
            raise
        return res

    # 错误提示
    def get_login_error(self):
        try:
            self.bs.show_waiting('//div[@id="layui-layer1"]/div[i]', 'XPATH')
            res = self.bs.find_xpath('//div[@id="layui-layer1"]/div[i]')
            # res =  self.bs.driver.find_element(by=By.XPATH,value='//div[@id="layui-layer1"]/div[i]')
        except Exception:
            self.log.getLog(element='查找"错误提示"失败')
            raise
        return res

    # 登录按钮
    def get_login_sbtbutton(self):
        try:
            res = self.bs.find_xpath('//a[@name="sbtbutton"]').click()
            # res = self.bs.driver.find_element(by=By.XPATH, value='//a[@name="sbtbutton"]').click()
        except Exception:
            self.log.getLog(element='查找"登录按钮"失败')
            raise
        return res

    # 登录成功提示
    def get_login_success(self):
        try:
            self.bs.show_waiting('//div[contains(@class,"mu-midd")]/a[contains(@class,"mu-m-phone")]', 'XPATH')
            res = self.bs.find_xpath('//div[contains(@class,"mu-midd")]/a[contains(@class,"mu-m-phone")]')
            # res = self.bs.driver.find_element(by=By.XPATH, value='//div[contains(@class,"mu-midd")]/a[contains(@class,"mu-m-phone")]')
        except Exception:
            self.log.getLog(element='查找"登录成功提示"失败')
            raise
        return res