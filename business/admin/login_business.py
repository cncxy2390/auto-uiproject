from handle.admin.login_handle import LoginHandle


class LoginBusiness(object):

    def __init__(self):
        self.lh = LoginHandle()

    # 正常登录
    def common_login(self, username, password, code):
        self.lh.send_login_unsername(username=username)
        self.lh.send_login_password(password=password)
        self.lh.send_login_code(code=code)

    # 登录成功
    def login_success(self, username, password, code):
        self.common_login(username, password, code)
        self.lh.click_login_submit()
        res = self.lh.get_login_text('登录成功')
        return res

    # 用户名错误
    def login_username_error(self, username, password, code):
        self.common_login(username=username, password=password, code=code)
        self.lh.click_login_submit()
        res =  self.lh.get_login_text('账号密码不正确!')
        return res


    # 用户名为空
    def login_username_null(self, username, password, code):
        self.common_login(username=username, password=password, code=code)
        self.lh.click_login_submit()
        res =  self.lh.get_login_text('用户名提示语')
        return res[2:]


    # 密码错误
    def login_password_error(self, username, password, code):
        self.common_login(username=username, password=password, code=code)
        self.lh.click_login_submit()
        res = self.lh.get_login_text('账号密码不正确!')
        return res

    # 密码为空
    def login_password_null(self, username, password, code):
        self.common_login(username=username, password=password, code=code)
        self.lh.click_login_submit()
        res = self.lh.get_login_text('密码提示语')
        return res[2:]

    # 验证码为空
    def login_code_null(self, username, password, code):
        self.common_login(username=username, password=password, code=code)
        self.lh.click_login_submit()
        res = self.lh.get_login_text('验证码为空')
        return res
