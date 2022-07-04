import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Bases(object):

    def __init__(self):
        option = webdriver.ChromeOptions()
        option.add_experimental_option('detach',True)
        self.driver = webdriver.Chrome(options=option)
        self.driver.maximize_window()

    # 登录
    def login(self,username='13026574581', password='qwert12345', code='yyds'):
        self.driver.refresh()
        self.driver.get('http://tpshop.cn/Home/user/login')
        self.driver.find_element(by=By.ID,value='username').send_keys(username)
        self.driver.find_element(by=By.ID,value='password').send_keys(password)
        self.driver.find_element(by=By.ID,value='verify_code').send_keys(code)
        time.sleep(0.3)
        self.driver.find_element(by=By.XPATH,value='//a[@name="sbtbutton"]').click()


    # id定位
    def find_id(self, value):
        return self.driver.find_element(by=By.ID, value=value)

    # xpath定位
    def find_xpath(self, value):
        return self.driver.find_element(by=By.XPATH, value=value)

    # name定位
    def find_name(self, value):
        return self.driver.find_element(by=By.NAME, value=value)


    # 切换iframe
    def switch_to_iframe(self, frame_reference):
        return self.driver.switch_to.frame(frame_reference)

    # 切换iframe
    def switch_default_content_iframe(self,):
        return self.driver.switch_to.default_content()


    # 显示等待
    def show_waiting(self, xpath, flag):
        wait = WebDriverWait(self.driver, 10, 0.1)
        if flag == 'XPATH':
            try:
                locator = (By.XPATH, xpath)
                wait.until(EC.presence_of_element_located(locator))
            except TimeoutError as te:
                print('XPATH:示等待超时')
                raise te
        elif flag == 'ID':
            try:
                locator = (By.ID, xpath)
                wait.until(EC.presence_of_element_located(locator))
            except TimeoutError as te:
                print('ID:显示等待超时')
                raise te

    # 获取会员等级
    def get_member_grade(self):
        self.show_waiting('//a[@class="mu-m-vip"]', 'XPATH')
        return self.driver.find_element(by=By.XPATH, value='//a[@class="mu-m-vip"]').get_attribute('textContent')

    # 返回首页
    def back_home(self):
        self.member_grade = self.get_member_grade()
        self.show_waiting('//div[@class="ecsc-logo"]', 'XPATH')
        self.driver.find_element(by=By.XPATH, value='//div[@class="ecsc-logo"]').click()

    # 获取alert弹窗
    def get_alert(self):
        return self.driver.switch_to.alert.accept()