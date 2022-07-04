from selenium.webdriver.common.by import By
from common.bases import Bases
from common.logger import Logger


class LoginPage(object):

    def __init__(self):
        self.bs = Bases()
        self.log = Logger()

    # 登录成功
    def get_login_success(self):
        try:
            res = self.bs.find_xpath('//span[@class="bgdopa-t"]')
            # res = self.bs.driver.find_element(by=By.XPATH, value='//span[@class="bgdopa-t"]')
        except Exception:
            self.log.getLog(element='查找"登录成功"失败')
            raise
        return res

    # 用户名
    def get_login_username(self):
        try:
            res = self.bs.find_xpath('//input[@name="username"]')
            # res = self.bs.driver.find_element(by=By.XPATH, value='//input[@name="username"]')
        except Exception:
            self.log.getLog(element='查找"用户名"失败')
            raise
        return res

    # 密码
    def get_login_password(self):
        try:
            res = self.bs.find_xpath('//input[@name="password"]')
            # res = self.bs.driver.find_element(by=By.XPATH, value='//input[@name="password"]')
        except Exception:
            self.log.getLog(element='查找"密码"失败')
            raise
        return res

    # 验证码
    def get_login_code(self):
        try:
            res = self.bs.find_xpath('//input[@name="vertify"]')
            # res = self.bs.driver.find_element(by=By.XPATH, value='//input[@name="vertify"]')
        except Exception:
            self.log.getLog(element='查找"验证码"失败')
            raise
        return res

    # 登录按钮
    def get_login_submit(self):
        try:
            res = self.bs.find_name('submit').click()
            # res = self.bs.driver.find_element(by=By.NAME, value='submit').click()
        except Exception:
            self.log.getLog(element='查找"登录按钮"失败')
            raise
        return res

    # 账号密码不正确
    def get_login_username_password_error(self):
        try:
            res = self.bs.find_xpath('//span[@class="error"]')
            # res = self.bs.driver.find_element(by=By.XPATH, value='//span[@class="error"]')
        except Exception:
            self.log.getLog(element='查找"账号密码不正确"失败')
            raise
        return res

    # 用户名提示语
    def get_login_username_error(self):
        try:
            res = self.bs.find_xpath('//span[@class="error"]')
            # res = self.bs.driver.find_element(by=By.XPATH, value='//span[@class="error"]')
        except Exception:
            self.log.getLog(element='查找"用户名提示语"失败')
            raise
        return res

    # 密码提示语
    def get_login_password_error(self):
        try:
            res = self.bs.find_xpath('//span[@class="error"]')
            # res = self.bs.driver.find_element(by=By.XPATH, value='//span[@class="error"]')
        except Exception:
            self.log.getLog(element='查找"密码提示语"失败')
            raise
        return res

    # 验证码提示语
    def get_login_code_error(self):
        try:
            res = self.bs.find_xpath('//span[@class="error"]')
            # res = self.bs.driver.find_element(by=By.XPATH, value='//span[@class="error"]')
        except Exception:
            self.log.getLog(element='查找"验证码提示语"失败')
            raise
        return res