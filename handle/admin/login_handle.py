from page.admin.login_page import LoginPage


class LoginHandle(object):

    def __init__(self):
        self.login = LoginPage()


    # 输入用户名
    def send_login_unsername(self, username):
        self.login.get_login_username().send_keys(username)

    # 输入密码
    def send_login_password(self, password):
        self.login.get_login_password().send_keys(password)

    # 输入验证码
    def send_login_code(self, code):
        self.login.get_login_code().send_keys(code)

    # 点击登录按钮
    def click_login_submit(self):
        self.login.get_login_submit()

    # 获取错误提示
    def get_login_text(self, error_info):
        text = None
        if error_info == '登录成功':
            text = self.login.get_login_success().get_attribute('textContent')
        elif error_info == '账号密码不正确!':
            text = self.login.get_login_username_password_error().get_attribute('textContent')
        elif error_info == '用户名提示语':
            text = self.login.get_login_username_error().get_attribute('textContent')
        elif error_info == '密码提示语':
            text = self.login.get_login_password_error().get_attribute('textContent')
        elif error_info == '验证码为空':
            text = self.login.get_login_password_error().get_attribute('textContent')
        else:
            print('无法定位元素')
        return text