from page.login_reception_page import LoginReceptionPage

class LoginHandle(object):

    def __init__(self):
        self.lrp = LoginReceptionPage()

    # 输入用户名
    def send_login_username(self, username):
        return self.lrp.get_login_username().send_keys(username)

    # 输入密码
    def send_login_password(self, password):
        return self.lrp.get_login_password().send_keys(password)

    # 输入验证码
    def send_login_code(self, code):
        return self.lrp.get_login_code().send_keys(code)

    # 点击登录
    def cilck_login_sbtbutton(self):
        self.lrp.get_login_sbtbutton()

    # 获取错误提示
    def get_login_text(self, error_info):
        text = None
        if error_info == '登录成功':
            text = self.lrp.get_login_success().get_attribute('textContent')
        elif error_info == '用户名为空':
            text = self.lrp.get_login_error().get_attribute('textContent')
        elif error_info == '账号不存在':
            text = self.lrp.get_login_error().get_attribute('textContent')
        elif error_info == '账号格式不匹配':
            text = self.lrp.get_login_error().get_attribute('textContent')
        elif error_info == '密码为空':
            text = self.lrp.get_login_error().get_attribute('textContent')
        elif error_info == '密码错误':
            text = self.lrp.get_login_error().get_attribute('textContent')
        elif error_info == '验证码为空':
            text = self.lrp.get_login_error().get_attribute('textContent')
        else:
            print('元素无法定位')
        return text