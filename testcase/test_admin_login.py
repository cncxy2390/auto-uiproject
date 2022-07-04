import allure
import pytest

@allure.feature('后台登录')
class TestAdminLogin(object):

    # 用户名错误
    #         username = 'admin'
    #         password = 'qwert12345'
    #         code = 'yyds'
    # @pytest.mark.skip
    @allure.story('用户名错误')
    def test_username_error(self, admin_login, get_logger):
        username = 'adminff'
        password = 'qwert12345'
        code = 'yyds'
        expected = '账号密码不正确!'
        admin_login.lh.login.bs.driver.get('http://www.tpshop.cn/Admin/Admin/login.html')
        actual = admin_login.login_username_error(username, password, code)
        try:
            get_logger.getLog(username=username, password=password, code=code, actual=actual, expected=expected)
            assert actual == expected
        except AssertionError as e:
            raise e

    # 用户名为空
    # @pytest.mark.skip
    @allure.story('用户名为空')
    def test_username_null(self, admin_login, get_logger):
        username = ''
        password = 'qwert12345'
        code = 'yyds'
        expected = '用户名不能为空'
        admin_login.lh.login.bs.driver.get('http://www.tpshop.cn/Admin/Admin/login.html')
        actual = admin_login.login_username_null(username, password, code)
        actual = actual[0:]
        try:
            get_logger.getLog(username=username, password=password, code=code, actual=actual, expected=expected)
            assert actual == expected
        except AssertionError as e:
            raise e


    # 密码错误
    # @pytest.mark.skip
    @allure.story('密码错误')
    def test_password_error(self, admin_login, get_logger):
        username = 'admin'
        password = 'qwert12345ff'
        code = 'yyds'
        expected = '账号密码不正确!'
        admin_login.lh.login.bs.driver.get('http://www.tpshop.cn/Admin/Admin/login.html')
        actual = admin_login.login_password_error(username, password, code)
        try:
            get_logger.getLog(username=username, password=password, code=code, actual=actual, expected=expected)
            assert actual == expected
        except AssertionError as e:
            raise e

    # 密码为空
    # @pytest.mark.skip
    @allure.story('密码为空')
    def test_password_null(self, admin_login, get_logger):
        username = 'admin'
        password = ''
        code = 'yyds'
        expected = '密码不能为空'
        admin_login.lh.login.bs.driver.get('http://www.tpshop.cn/Admin/Admin/login.html')
        actual = admin_login.login_password_null(username, password, code)
        actual = actual[0:]
        try:
            get_logger.getLog(username=username, password=password, code=code, actual=actual, expected=expected)
            assert actual == expected
        except AssertionError as e:
            raise e

    # 验证码为空
    # @pytest.mark.skip
    @allure.story('验证码为空')
    def test_code_null(self, admin_login, get_logger):
        username = 'admin'
        password = 'qwert12345'
        code = ''
        expected = '验证码不能为空'
        admin_login.lh.login.bs.driver.get('http://www.tpshop.cn/Admin/Admin/login.html')
        actual = admin_login.login_code_null(username, password, code)
        actual = actual[2:]
        try:
            get_logger.getLog(username=username, password=password, code=code, actual=actual, expected=expected)
            assert actual == expected
        except AssertionError as e:
            raise e

    # 登录成功
    # @pytest.mark.skip
    @allure.story('登录成功')
    def test_login_success(self, admin_login, get_logger):
        username = 'admin'
        password = 'qwert12345'
        code = 'yyds'
        expected = 'admin'
        admin_login.lh.login.bs.driver.get('http://www.tpshop.cn/Admin/Admin/login.html')
        actual = admin_login.login_success(username, password, code)
        try:
            get_logger.getLog(username=username, password=password, code=code, actual=actual, expected=expected)
            assert actual == expected
        except AssertionError as e:
            raise e

if __name__ == '__main__':
    pytest.main()