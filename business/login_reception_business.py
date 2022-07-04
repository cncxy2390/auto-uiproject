from handle.login_handle import LoginHandle

class LoginReceptionBusiness(object):

    def __init__(self):
        self.lh = LoginHandle()


    # 正常登录
    def common_login(self, username, password, code):
        self.lh.send_login_username(username=username)
        self.lh.send_login_password(password=password)
        self.lh.send_login_code(code=code)

    # 登录成功
    def login_success(self, username, password, code):
        self.common_login(username, password, code)
        self.lh.cilck_login_sbtbutton()
        res = self.lh.get_login_text('登录成功')
        return res

    # 手机号/邮箱不存在 does not exist
    def login_username_not_exist(self, username, password, code):
        self.common_login(username, password, code)
        self.lh.cilck_login_sbtbutton()
        res = self.lh.get_login_text('账号不存在')
        return res


    # 手机号/邮箱为空
    def login_username_null(self, username, password, code):
        self.common_login(username, password, code)
        self.lh.cilck_login_sbtbutton()
        res = self.lh.get_login_text('用户名为空')
        return res

    # 手机号/邮箱格式不匹配
    def login_username_format(self, username, password, code):
        self.common_login(username, password, code)
        self.lh.cilck_login_sbtbutton()
        res = self.lh.get_login_text('账号格式不匹配')
        return res

    # 密码错误
    def login_password_error(self, username, password, code):
        self.common_login(username, password, code)
        self.lh.cilck_login_sbtbutton()
        res = self.lh.get_login_text('密码错误')
        return res

    # 密码为空
    def login_password_null(self, username, password, code):
        self.common_login(username, password, code)
        self.lh.cilck_login_sbtbutton()
        res = self.lh.get_login_text('密码为空')
        return res

    # 验证码为空
    def login_code_null(self, username, password, code):
        self.common_login(username, password, code)
        self.lh.cilck_login_sbtbutton()
        res = self.lh.get_login_text('验证码为空')
        return res
